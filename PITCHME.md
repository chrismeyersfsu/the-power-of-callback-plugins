<!-- .element: class="x" -->

<img src="./assets/md/assets/img/callback-boy.gif" class="meme"/>


<pre style="box-shadow: none; font-weight: bold; padding: 0 20%;">
  ^__^
  (oo)\_______
  (__)\       )\/\
      ||----w |
      ||     ||
</pre>

### <span class="yaml-dash">-</span>name: The Power of Callback Plugins
#### hosts: AnsibleFest San Francisco 2017
#### vars:
#### &nbsp;&nbsp;presenter: Chris Church
#### <!-- .element: class="fragment" -->tasks: ...


Note:
Do I need a note?

+++

<img src="./assets/md/assets/img/who-dis.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Who Dis?
#### set_fact:
#### <!-- .element: class="fragment" -->&nbsp;&nbsp;`tower_api_developer`: > <br/> &nbsp;&nbsp;&nbsp;&nbsp;[Since March 2013](https://github.com/ansible/awx/commit/a61a3538291812de5032bc383e662c000e33741e)
#### <!-- .element: class="fragment" -->&nbsp;&nbsp;`tower_callback_plugin`: > <br/> &nbsp;&nbsp;&nbsp;&nbsp;[~90% of current implementation](https://github.com/ansible/awx/blame/c7a85d9738a1e7ddd52a65968766800ed8c34d12/awx/lib/tower_display_callback/module.py)
#### <!-- .element: class="fragment" -->&nbsp;&nbsp;`ansible_winning: >` <br/> &nbsp;&nbsp;&nbsp;&nbsp;[github.com/cchurch/ansible-winning](https://github.com/cchurch/ansible-winning)
#### <!-- .element: class="fragment" --><img src="./assets/md/assets/img/ansible-sign.gif" style="position: absolute; top: 145px; right: -35px; clip: rect(45px,230px,235px,35px);"/>&nbsp;&nbsp;`ansible_sign: >` <br/> &nbsp;&nbsp;&nbsp;&nbsp;[github.com/cchurch/ansible-sign](https://github.com/cchurch/ansible-sign)

Note:

---

<img src="./assets/md/assets/img/tower-fall.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: How Tower Runs a Job
#### hosts: Ansible Tower
#### tasks: ...

<!--  <img src="./assets/md/assets/img/awx-logo.svg" style="border: none; box-shadow: none; width: 50%;"/> -->

Note:

+++

<img src="./assets/md/assets/img/templates-ui.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Job Templates UI
#### `get_url`: <br/>&nbsp;&nbsp;url: [tower/#/templates/job_template/N](https://tower/#/templates/job_template/1)

<iframe class="fragment" x-src="https://tower.ninemoreminutes.com/#/templates/job_template/80"></iframe>

+++

<img src="./assets/md/assets/img/templates-api.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Job Templates API
#### `get_url`: <br/>&nbsp;&nbsp;url: [tower/api/v1/job_templates/N/](https://tower/api/v1/job_templates/1/)

<iframe class="fragment" x-src="https://tower.ninemoreminutes.com/api/v1/job_templates/80/"></iframe>

+++

<img src="./assets/md/assets/img/ansible-help.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Playbook Options
#### command: ansible-playbook --help

<pre class="fragment" style="font-size: 0.4em; margin-top: 5em;"><code class="console">
Usage: ansible-playbook playbook.yml

Options:
  --ask-become-pass     ask for privilege escalation password
  -k, --ask-pass        ask for SSH password
  --ask-su-pass         ask for su password (deprecated, use become)
  -K, --ask-sudo-pass   ask for sudo password (deprecated, use become)
  --ask-vault-pass      ask for vault password
  -b, --become          run operations with become (nopasswd implied)
  --become-method=BECOME_METHOD
                        privilege escalation method to use (default=sudo),
                        valid choices: [ sudo | su | pbrun | pfexec | runas ]
  --become-user=BECOME_USER
                        run operations as this user (default=None)
  -C, --check           don't make any changes; instead, try to predict some
                        of the changes that may occur
  -c CONNECTION, --connection=CONNECTION
                        connection type to use (default=smart)
  -D, --diff            when changing (small) files and templates, show the
                        differences in those files; works great with --check
  -e EXTRA_VARS, --extra-vars=EXTRA_VARS
                        set additional variables as key=value or YAML/JSON
  --flush-cache         clear the fact cache
  --force-handlers      run handlers even if a task fails
  -f FORKS, --forks=FORKS
                        specify number of parallel processes to use
                        (default=5)
  -h, --help            show this help message and exit
  -i INVENTORY, --inventory-file=INVENTORY
                        specify inventory host file
                        (default=/etc/ansible/hosts)
  -l SUBSET, --limit=SUBSET
                        further limit selected hosts to an additional pattern
  --list-hosts          outputs a list of matching hosts; does not execute
                        anything else
  --list-tags           list all available tags
  --list-tasks          list all tasks that would be executed
  -M MODULE_PATH, --module-path=MODULE_PATH
                        specify path(s) to module library (default=None)
  --private-key=PRIVATE_KEY_FILE
                        use this file to authenticate the connection
  --skip-tags=SKIP_TAGS
                        only run plays and tasks whose tags do not match these
                        values
  --start-at-task=START_AT
                        start the playbook at the task matching this name
  --step                one-step-at-a-time: confirm each task before running
  -S, --su              run operations with su (deprecated, use become)
  -R SU_USER, --su-user=SU_USER
                        run operations with su as this user (default=root)
                        (deprecated, use become)
  -s, --sudo            run operations with sudo (nopasswd) (deprecated, use
                        become)
  -U SUDO_USER, --sudo-user=SUDO_USER
                        desired sudo user (default=root) (deprecated, use
                        become)
  --syntax-check        perform a syntax check on the playbook, but do not
                        execute it
  -t TAGS, --tags=TAGS  only run plays and tasks tagged with these values
  -T TIMEOUT, --timeout=TIMEOUT
                        override the SSH timeout in seconds (default=10)
  -u REMOTE_USER, --user=REMOTE_USER
                        connect as this user (default=chris)
  --vault-password-file=VAULT_PASSWORD_FILE
                        vault password file
  -v, --verbose         verbose mode (-vvv for more, -vvvv to enable
                        connection debugging)
  --version             show program's version number and exit
</code></pre>

+++

<img src="./assets/md/assets/img/launch-job.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Launch a Job
#### `get_url`: <br/>&nbsp;&nbsp;url: [tower/#/jobs/N](https://tower/#/jobs/1)

<iframe class="fragment" x-src="https://tower.ninemoreminutes.com/#/templates?template_search=id__icontains_DEFAULT:80"></iframe>

+++

<img src="./assets/md/assets/img/jobs-api.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Jobs API
#### `get_url`: <br/>&nbsp;&nbsp;url: [tower/api/v1/jobs/N/](https://tower/api/v1/jobs/1/)

<iframe class="fragment" x-src="https://tower.ninemoreminutes.com/api/v1/jobs/?order_by=-id"></iframe>

+++

<img src="./assets/md/assets/img/job-events-api.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Job Events API
#### `get_url`: <br/>&nbsp;&nbsp;url: [tower/api/v1/jobs/N/job_events/](https://tower/api/v1/jobs/1/job_events/)

<iframe class="fragment" x-src="https://tower.ninemoreminutes.com/api/v1/jobs/?order_by=-id"></iframe>

---

<img src="./assets/md/assets/img/what-is.gif" class="meme" style="top: 100px;"/>

### <span class="yaml-dash">-</span>name: What *IS* a Callback Plugin?
#### hosts: Ansible Core
#### tasks: ...

+++

<img src="./assets/md/assets/img/plugins.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: One of Many Plugins
#### command: ><br/>&nbsp;&nbsp;find -type d lib/ansible/plugins/

<div style="position: relative;">
<pre class="fragment current-visible" style="position: absolute;"><code class="ini">action
cache
callback
connection
filter
lookup
shell
strategy
terminal
test
vars
</code></pre>

<div class="fragment current-visible" style="position: absolute;">
<p>Also Plugins:</p>
<ul>
  <li>modules</li>
  <li>module_utils</li>
  <li>module_doc_fragments</li>
</ul>
</div>

<div class="fragment current-visible" style="position: absolute;">
<p>More in 2.4:</p>
<ul>
  <li>cliconf</li>
  <li>inventory</li>
  <li>netconf</li>
</ul>
</div>

</div>

+++

<img src="./assets/md/assets/img/callback-base.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: CallbackBase
#### debug:<br/>&nbsp;&nbsp;var: ansible.plugins.callback.CallbackBase

<pre class="fragment"><code class="python hljs">class CallbackBase:

    CALLBACK_VERSION: '2.0'
    CALLBACK_TYPE: 'notification'
    CALLBACK_NAME: 'myplugin'
    CALLBACK_NEEDS_WHITELIST: True

</code><code class="fragment python hljs">    def v2_on_any(self, *args, **kwargs):
        pass
</code></pre>

+++

<img src="./assets/md/assets/img/callback-type.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: CALLBACK_TYPE
#### debug:<br/>&nbsp;&nbsp;var: CallbackBase.CALLBACK_TYPE

<ul class="fragment" style="margin-top: 1em;">
  <li><b>stdout</b>: Only one</li>
  <li><b>notification</b>: Zero or more, may be whitelisted</li>
  <li><b>aggregate</b>: Zero or more, may be whitelisted</li>
</ul>

+++

<div><img src="./assets/md/assets/img/built-in.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Built-In Callbacks
#### command: ><br/>&nbsp;&nbsp;ls lib/ansible/plugins/callback/*.py

<div style="position: relative;">

<div class="fragment current-visible" style="position: absolute; width: 100%;">
<p>Stdout:</p>
<pre><code class="ini">default (ansible-playbook)
minimal (ansible, ansible-console)
actionable
debug
dense
fullskip
json
oneline
selective
skippy
stderr
</code></pre>
</div>

<div class="fragment current-visible" style="position: absolute;; width: 100%;">
<p>Notification:</p>
<pre><code class="ini">foreman
hipchat
jabber
log_plays
logentries
mail
osx_say
slack
</code></pre>
</div>

<div class="fragment current-visible" style="position: absolute;; width: 100%;">
<p>Aggregate:</p>
<pre><code class="ini">context_demo
junit
logstash
profile_roles
profile_tasks
syslog_json
timer
tree
</code></pre>
</div>

</div>

+++

<div><img src="./assets/md/assets/img/bring-your-own.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Bring Your Own
#### debug: var=callback_plugins

<div class="fragment">
<p>Playbooks and Roles:</p>
<pre><code class="jinja">{{playbook_dir}}/callback_plugins
{{role_dir}}/callback_plugins
</code></pre>
</div>

<div class="fragment">
<p>ANSIBLE_CALLBACK_PLUGINS or ansible.cfg:</p>

<pre><code class="ini">[defaults]
callback_plugins=~/.ansible/plugins/callback:/usr/share/ansible/plugins/callback
</code></pre>
</div>

+++

<div><img src="./assets/md/assets/img/loaded-when.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Loaded When?
#### debug: msg='Callback Loaded'<br/>when: CALLBACK_TYPE == 'stdout'

<div class="fragment">
<p>ANSIBLE_STDOUT_CALLBACK or ansible.cfg:</p>
<pre><code class="ini">[defaults]
stdout_callback=default
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: msg='Callback Loaded'<br/>when: CALLBACK_TYPE != 'stdout'</h4>
<p>CALLBACK_NEEDS_WHITELIST == False or<br/>ANSIBLE_CALLBACK_WHITELIST or ansible.cfg:</p>
<pre><code class="ini">[defaults]
callback_whitelist=timer,tree
</code></pre>
</div>

---

<div><img src="./assets/md/assets/img/playbooks-plays-tasks.gif" class="meme" style="top: 100px;"/></div>

### <span class="yaml-dash">-</span>name: Playbooks, Plays & Tasks
#### hosts: Demo Callback Plugin
#### tasks: ...

+++

### <span class="yaml-dash">-</span>name: Once Per Playbook
#### `debug: var=v2_playbook_on_start`

```python
    def v2_playbook_on_start(self, playbook):
        filename = getattr(playbook, '_file_name', '???')
```

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=v2_playbook_on_start_stdout</h4>
<pre><code class="hljs"></code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=v2_runner_on_ok</h4>
<pre><code class="lang-python hljs">    def v2_playbook_on_start(self, playbook):
        filename = getattr(playbook, '_file_name', '???')
</code></pre>
</div>


+++

### <span class="yaml-dash">-</span>name: I Haz Questions
#### debug:
        msg: v2_playbook_on_vars_prompt(varname, private=True, prompt=None, encrypt=None, confirm=False, salt_size=None, salt=None, default=None)

+++

### <span class="yaml-dash">-</span>name: Some Other Thing
#### debug:
        msg: v2_playbook_on_include(included_file) - included_file._filename
        
+++

### <span class="yaml-dash">-</span>name: Play Ball
#### debug:
        msg: v2_playbook_on_play_start(play) - play.hosts (str or list), play.get_name(), play._uuid

+++

### <span class="yaml-dash">-</span>name: Task It
#### debug:
        msg: >
          v2_playbook_on_task_start(task, is_conditional) - task._uuid,
          task.get_name(), task.name, task.action, task.get_path(), task.no_log,
          task.args, task._role._role_name or task.role_name

+++

### <span class="yaml-dash">-</span>name: Handle It
#### debug:
        msg: v2_playbook_on_handler_task_start(task) ~= v2_playbook_on_task_start(task, True)

+++

### <span class="yaml-dash">-</span>name: No Hosts
#### debug:
        msg: v2_playbook_on_no_hosts_matched()

+++

### <span class="yaml-dash">-</span>name: No Hosts Remaining
#### debug:
        msg: v2_playbook_on_no_hosts_remaining

+++

<img src="./assets/md/assets/img/playbook-stats.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Statistically Speaking
#### debug:
        msg: v2_playbook_on_stats(stats) - stats.changed, stats.dark, stats.failures, stats.ok, stats.processed, stats.skipped, getattr(stats, 'custom', {})

---

### <span class="yaml-dash">-</span>name: Runner Events
#### hosts: Callback Plugin Demo
#### tasks: ...

+++

<img src="./assets/md/assets/img/runner-ok.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: OK
#### debug: var=`ok_task`

<pre><code class="yaml hljs">- command: uptime</code></pre>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=ok_stdout</h4>
<pre><code class="hljs">
  ok: [me] => </code><code class="json hljs">{"changed": false, "cmd": ["uptime"], "delta": "0:00:00.012216", "end": "2017-08-29 15:18:07.139319", "rc": 0, "start": "2017-08-29 15:18:07.127103", "stderr": "", "stderr_lines": [], "stdout": "15:18  up 7 days, 23:02, 12 users, load averages: 2.51 2.22 2.27", "stdout_lines": ["15:18  up 7 days, 23:02, 12 users, load averages: 2.51 2.22 2.27"]}
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=v2_runner_on_ok</h4>
<pre><code class="lang-python hljs">    def v2_runner_on_ok(self, result):
        filename = getattr(playbook, '_file_name', '???')
</code></pre>
</div>

+++

### <span class="yaml-dash">-</span>name: Failed
#### debug:<br/>&nbsp;&nbsp;var: `v2_runner_on_failed`

```python
    def v2_runner_on_failed(self, result):
        filename = getattr(playbook, '_file_name', '???')
```

+++

<img src="./assets/md/assets/img/runner-skipped.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Skipped
#### debug:<br/>&nbsp;&nbsp;var: `v2_runner_on_skipped`

```python
    def v2_runner_on_skipped(self, result):
        filename = getattr(playbook, '_file_name', '???')
```

+++

<img src="./assets/md/assets/img/runner-unreachable.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Unreachable
#### debug:<br/>&nbsp;&nbsp;var: `v2_runner_on_unreachable`

+++

<img src="./assets/md/assets/img/runner-item-ok.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Item OK
#### debug: var=`v2_runner_item_on_ok`

+++

### <span class="yaml-dash">-</span>name: Item Failed
#### debug: var=`v2_runner_item_on_failed`

+++

### <span class="yaml-dash">-</span>name: Item Skipped
#### debug: var=`v2_runner_item_on_skipped`

+++

### <span class="yaml-dash">-</span>name: File Diff
#### debug:<br/>&nbsp;&nbsp;var: `v2_on_file_diff`

+++

### <span class="yaml-dash">-</span>name: Never Called
#### debug: var={{item}}<br/>when: false<br/>`with_items`:<br/>&nbsp;&nbsp;-&nbsp;`v2_playbook_on_notify`<br/>&nbsp;&nbsp;-&nbsp;`v2_playbook_on_no_hosts_matched`<br/>&nbsp;&nbsp;-&nbsp;`v2_playbook_on_cleanup_task_start`<br/>&nbsp;&nbsp;-&nbsp;`v2_runner_on_async_poll`<br/>&nbsp;&nbsp;-&nbsp;`v2_runner_on_async_ok`<br/>&nbsp;&nbsp;-&nbsp;`v2_runner_on_async_failed`<br/>&nbsp;&nbsp;-&nbsp;`v2_runner_on_file_diff`<br/>&nbsp;&nbsp;-&nbsp;`v2_runner_on_no_hosts`

---

### <span class="yaml-dash">-</span>name: What About?
#### hosts: Demo Callback Plugin
#### tasks: ...

+++

### <span class="yaml-dash">-</span>name: Capturing Stdout
#### debug: var=ansible.utils.display.Display

```
```

+++

<img src="./assets/md/assets/img/no-log.gif" class="meme"/>


### <span class="yaml-dash">-</span>name: My ⨍®𝒾¢₭ℹ︎ℵ§ Passwords



+++

### <span class="yaml-dash">-</span>name: 

---

<div><img src="./assets/md/assets/img/what-next.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: What Next?
#### hosts: You
#### tasks: ...

+++

### <span class="yaml-dash">-</span>name: AWX
#### get_url:<br/>&nbsp;&nbsp;url: [github.com/ansible/awx](https://github.com/ansible/awx)

#### <!-- .element: class="fragment" --><span class="yaml-dash">-</span>set_fact:<br/>&nbsp;&nbsp;google_group: [awx-project](https://groups.google.com/d/forum/awx-project)<br/>&nbsp;&nbsp;freenode_irc: [ansible-awx](irc://irc.freenode.net/ansible-awx)

+++

<div><img src="./assets/md/assets/img/fixme.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: FIXME
#### command: ><br>&nbsp;&nbsp;grep -hir fixme<br/>&nbsp;&nbsp;awx/lib/awx_display_callback/

<pre class="fragment" style="margin-top: 2em;"><code class="python"># FIXME: Task is "global" unless using free strategy!
# FIXME: Flag task path output as vv.
# FIXME: When this task UUID repeats, it means the play is using the free strategy...
# FIXME: Add count of plays/tasks.
# FIXME: Display detailed results or not based on verbosity.
# FIXME: Add verbosity for exception/results output.
</code></pre>

+++

<div><img src="./assets/md/assets/img/questions.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Contact Me
#### pause:<br/>&nbsp;&nbsp;prompt: Any questions?

#### <!-- .element: class="fragment" --><span class="yaml-dash">-</span>set_fact:<br/>&nbsp;&nbsp;github: [@cchurch](https://github.com/cchurch)<br/>&nbsp;&nbsp;twitter: [@flyingfred0](https://twitter.com/flyingfred0)<br/>&nbsp;&nbsp;email: [cchurch@redhat.com](mailto:cchurch@redhat.com)
#### <!-- .element: class="fragment" --><span class="yaml-dash">-</span>get_url:<br/>&nbsp;&nbsp;url: [cchurch/the-power-of-callback-plugins](https://github.com/cchurch/the-power-of-callback-plugins)
