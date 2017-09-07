# Python
from __future__ import (absolute_import, division, print_function)
import collections
from copy import copy
import datetime
import json
import os

# PyYAML
import yaml

# Ansible
from ansible.plugins.callback import CallbackBase


class CallbackModule(CallbackBase):
    '''
    Callback module for logging ansible/ansible-playbook events.
    '''

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'debug_events'

    def __init__(self):
        super(CallbackModule, self).__init__()
        self.event_context = collections.OrderedDict()
        self.event_filename = os.path.join(
            os.path.dirname(__file__),
            '..',
            'event_output',
            #'events_{}.jsonl'.format(datetime.datetime.now().isoformat()),
            'events_{}.yaml'.format(datetime.datetime.now().isoformat()),
        )
        if not os.path.isdir(os.path.dirname(self.event_filename)):
            os.makedirs(os.path.dirname(self.event_filename))
        self.event_output = open(self.event_filename, 'w')
        self.event_output.write('---\n\n')
        print('loaded!')

    def yaml_safe_dump(self, data, stream=None, Dumper=yaml.SafeDumper, **kwargs):
        kwargs.setdefault('default_flow_style', False)

        class OrderedDumper(Dumper):
            pass

        def _dict_representer(dumper, data):
            return dumper.represent_mapping(
                yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                data.items()
            )

        OrderedDumper.add_representer(collections.OrderedDict, _dict_representer)

        return yaml.dump(data, stream, OrderedDumper, **kwargs)

    def capture_event_data(self, event, event_data=None):
        event_data = event_data or collections.OrderedDict()
        new_event_data = collections.OrderedDict(self.event_context.items())
        for k, v in event_data.items():
            new_event_data[k] = v

        if new_event_data.get('res'):
            if new_event_data['res'].get('_ansible_no_log', False):
                new_event_data['res'] = {'censored': 'CENSORED'}
            if new_event_data['res'].get('results', []):
                new_event_data['res']['results'] = copy(new_event_data['res']['results'])
            for i, item in enumerate(new_event_data['res'].get('results', [])):
                if isinstance(item, dict) and item.get('_ansible_no_log', False):
                    event_data['res']['results'][i] = {'censored': 'CENSORED'}

        # FIXME!
        print(event, new_event_data)
        self.yaml_safe_dump([dict(event=event, event_data=new_event_data)],
                            self.event_output)

    def set_playbook(self, playbook):
        self.event_context['playbook_filename'] = getattr(playbook, '_file_name', '???')
        self.clear_play()

    def set_play(self, play):
        if hasattr(play, 'hosts'):
            if isinstance(play.hosts, list):
                pattern = ','.join(play.hosts)
            else:
                pattern = play.hosts
        else:
            pattern = ''
        self.event_context['play_name'] = play.get_name().strip() or pattern
        self.event_context['play_pattern'] = pattern
        self.event_context['play_uuid'] = str(play._uuid)
        self.clear_task()

    def clear_play(self):
        self.event_context.pop('play_name', None)
        self.event_context.pop('play_pattern', None)
        self.event_context.pop('play_uuid', None)
        self.clear_task()

    def set_task(self, task):
        self.event_context['task_name'] = task.name or task.action
        self.event_context['task_action'] = task.action
        self.event_context['task_uuid'] = str(task._uuid)
        try:
            self.event_context['task_path'] = task.get_path()
        except AttributeError:
            pass
        if task.no_log:
            task_args = 'NO LOG'
        else:
            task_args = ', '.join(('%s=%s' % a for a in task.args.items()))
        if task_args:
            self.event_context['task_args'] = task_args
        if getattr(task, '_role', None):
            task_role = task._role._role_name
        else:
            task_role = getattr(task, 'role_name', '')
        if task_role:
            self.event_context['task_role'] = task_role

    def clear_task(self):
        self.event_context.pop('task_name', None)
        self.event_context.pop('task_action', None)
        self.event_context.pop('task_uuid', None)
        self.event_context.pop('task_path', None)
        self.event_context.pop('task_args', None)
        self.event_context.pop('task_role', None)

    def v2_playbook_on_start(self, playbook):
        print(playbook, type(playbook))
        self.set_playbook(playbook)
        self.capture_event_data('v2_playbook_on_start')

    def v2_playbook_on_vars_prompt(self, varname, private=True, prompt=None,
                                   encrypt=None, confirm=False, salt_size=None,
                                   salt=None, default=None):
        event_data = collections.OrderedDict([
            ('varname', varname),
            ('private', private),
            ('prompt', prompt),
            ('encrypt', encrypt),
            ('confirm', confirm),
            ('salt_size', salt_size),
            ('salt', salt),
            ('default', default),
        ])
        self.capture_event_data('v2_playbook_on_vars_prompt', event_data)

    def v2_playbook_on_include(self, included_file):
        print('included_file=', included_file)
        try:
            filename = included_file._filename
            args = included_file._args
            task = included_file._task
            hosts = included_file._hosts
            print(filename, args, task, hosts)
        except AttributeError:
            pass
        event_data = collections.OrderedDict([
            ('included_file', included_file._filename if included_file is not None else None),
        ])
        self.capture_event_data('v2_playbook_on_include', event_data)

    def v2_playbook_on_play_start(self, play):
        self.set_play(play)
        self.capture_event_data('v2_playbook_on_play_start')

    def v2_playbook_on_import_for_host(self, result, imported_file):
        # NOTE: Not used by Ansible 2.x.
        self.capture_event_data('v2_playbook_on_import_for_host')

    def v2_playbook_on_not_import_for_host(self, result, missing_file):
        # NOTE: Not used by Ansible 2.x.
        self.capture_event_data('v2_playbook_on_not_import_for_host')

    def v2_playbook_on_setup(self):
        # NOTE: Not used by Ansible 2.x.
        self.capture_event_data('v2_playbook_on_setup')

    def v2_playbook_on_task_start(self, task, is_conditional):
        self.set_task(task)
        event_data = collections.OrderedDict([
            ('is_conditional', is_conditional),
        ])
        self.capture_event_data('v2_playbook_on_task_start', event_data)

    def v2_playbook_on_cleanup_task_start(self, task):
        # NOTE: Not used by Ansible 2.x.
        self.set_task(task)
        self.capture_event_data('v2_playbook_on_cleanup_task_start')

    def v2_playbook_on_handler_task_start(self, task):
        self.set_task(task)
        self.capture_event_data('v2_playbook_on_handler_task_start')

    def v2_playbook_on_no_hosts_matched(self):
        # NOTE: Not used by Ansible 2.x.
        self.capture_event_data('v2_playbook_on_no_hosts_matched')

    def v2_playbook_on_no_hosts_remaining(self):
        self.capture_event_data('v2_playbook_on_no_hosts_remaining')

    def v2_playbook_on_notify(self, result, handler):
        # NOTE: Not used by Ansible 2.x.
        event_data = collections.OrderedDict([
            ('host', result._host.get_name()),
            ('task', result._task),
            ('handler', handler),
        ])
        self.capture_event_data('v2_playbook_on_notify', event_data)

    def v2_playbook_on_stats(self, stats):
        self.clear_play()
        event_data = dict(
            changed=stats.changed,
            dark=stats.dark,
            failures=stats.failures,
            ok=stats.ok,
            processed=stats.processed,
            skipped=stats.skipped,
            custom=stats.custom.get('_run', {}) if hasattr(stats, 'custom') else {}
        )
        self.capture_event_data('v2_playbook_on_stats', event_data)

    def v2_runner_on_ok(self, result):
        print(json.dumps(result._result, indent=4, sort_keys=True))
        # FIXME: Display detailed results or not based on verbosity.

        # strip environment vars from the job event; it already exists on the
        # job and sensitive values are filtered there
        if result._task.action in ('setup', 'gather_facts'):
            result._result.get('ansible_facts', {}).pop('ansible_env', None)

        event_data = dict(
            host=result._host.get_name(),
            remote_addr=result._host.address,
            #task=result._task,
            res=result._result,
            event_loop=result._task.loop if hasattr(result._task, 'loop') else None,
        )
        self.capture_event_data('v2_runner_on_ok', event_data)

    def v2_runner_on_failed(self, result, ignore_errors=False):
        event_data = dict(
            host=result._host.get_name(),
            remote_addr=result._host.address,
            res=result._result,
            #task=result._task,
            ignore_errors=ignore_errors,
            event_loop=result._task.loop if hasattr(result._task, 'loop') else None,
        )
        self.capture_event_data('v2_runner_on_failed', event_data)

    def v2_runner_on_skipped(self, result):
        event_data = dict(
            host=result._host.get_name(),
            remote_addr=result._host.address,
            #task=result._task,
            event_loop=result._task.loop if hasattr(result._task, 'loop') else None,
        )
        self.capture_event_data('v2_runner_on_skipped', event_data)

    def v2_runner_on_unreachable(self, result):
        event_data = dict(
            host=result._host.get_name(),
            remote_addr=result._host.address,
            #task=result._task,
            res=result._result,
        )
        self.capture_event_data('v2_runner_on_unreachable', event_data)

    def v2_runner_on_no_hosts(self, task):
        # NOTE: Not used by Ansible 2.x.
        event_data = dict(
            #task=task,
        )
        self.capture_event_data('v2_runner_on_no_hosts', event_data)

    def v2_runner_on_async_poll(self, result):
        # NOTE: Not used by Ansible 2.x.
        event_data = dict(
            host=result._host.get_name(),
            task=result._task,
            res=result._result,
            jid=result._result.get('ansible_job_id'),
        )
        #with self.capture_event_data('runner_on_async_poll', **event_data):
        #    super(BaseCallbackModule, self).v2_runner_on_async_poll(result)

    def v2_runner_on_async_ok(self, result):
        # NOTE: Not used by Ansible 2.x.
        event_data = dict(
            host=result._host.get_name(),
            task=result._task,
            res=result._result,
            jid=result._result.get('ansible_job_id'),
        )
        #with self.capture_event_data('runner_on_async_ok', **event_data):
        #    super(BaseCallbackModule, self).v2_runner_on_async_ok(result)

    def v2_runner_on_async_failed(self, result):
        # NOTE: Not used by Ansible 2.x.
        event_data = dict(
            host=result._host.get_name(),
            task=result._task,
            res=result._result,
            jid=result._result.get('ansible_job_id'),
        )
        #with self.capture_event_data('runner_on_async_failed', **event_data):
        #    super(BaseCallbackModule, self).v2_runner_on_async_failed(result)

    def v2_runner_on_file_diff(self, result, diff):
        # NOTE: Not used by Ansible 2.x.
        event_data = dict(
            host=result._host.get_name(),
            task=result._task,
            diff=diff,
        )
        #with self.capture_event_data('runner_on_file_diff', **event_data):
        #    super(BaseCallbackModule, self).v2_runner_on_file_diff(result, diff)

    def v2_on_file_diff(self, result):
        # NOTE: Logged as runner_on_file_diff.
        event_data = dict(
            host=result._host.get_name(),
            #task=result._task,
            diff=result._result.get('diff'),
        )
        self.capture_event_data('v2_on_file_diff', event_data)

    def v2_runner_item_on_ok(self, result):
        event_data = dict(
            host=result._host.get_name(),
            #task=result._task,
            res=result._result,
        )
        self.capture_event_data('v2_runner_item_on_ok', event_data)

    def v2_runner_item_on_failed(self, result):
        event_data = dict(
            host=result._host.get_name(),
            #task=result._task,
            res=result._result,
        )
        self.capture_event_data('v2_runner_item_on_failed', event_data)

    def v2_runner_item_on_skipped(self, result):
        event_data = dict(
            host=result._host.get_name(),
            #task=result._task,
            res=result._result,
        )
        self.capture_event_data('v2_runner_item_on_skipped', event_data)

    def v2_runner_retry(self, result):
        event_data = dict(
            host=result._host.get_name(),
            #task=result._task,
            res=result._result,
        )
        self.capture_event_data('v2_runner_retry', event_data)
