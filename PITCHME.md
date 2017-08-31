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

<img src="./assets/md/assets/img/awx-logo.svg" style="border: none; box-shadow: none; width: 50%;"/>

Note:

+++

<img src="./assets/md/assets/img/templates-ui.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Job Templates UI
#### `get_url`: <br/>&nbsp;&nbsp;url: tower/#/templates/job_template/N

<img src="" alt="Job Templates UI Image"/>

+++

<img src="./assets/md/assets/img/templates-api.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Job Templates API
#### `get_url`: <br/>&nbsp;&nbsp;url: tower/api/v1/job_templates/N/

<img src="" alt="Job Templates API Image"/>

<!-- <iframe src="https://tower.testing.ansible.com/" width="400" height="300">FIXME</iframe> -->

+++

### <span class="yaml-dash">-</span>name: Ansible Playbook Options
#### command: ansible-playbook --help

```
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
```

+++

<img src="./assets/md/assets/img/launch-job.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Launch a Job
#### `get_url`: <br/>&nbsp;&nbsp;url: tower/#/jobs/N

<img src="" alt="Job Launch UI Image"/>

+++

<img src="./assets/md/assets/img/jobs-api.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Jobs API
#### `get_url`: <br/>&nbsp;&nbsp;url: tower/api/v1/jobs/N/

<img src="" alt="Job API Image"/>

+++

<img src="./assets/md/assets/img/job-events-api.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Job Events API
#### `get_url`: <br/>&nbsp;&nbsp;url: tower/api/v1/jobs/N/job_events/

<img src="" alt="Job Events API Image"/>

---

### <span class="yaml-dash">-</span>name: What **IS** a Callback Plugin?
#### hosts: Ansible Core
#### tasks: ...

+++

### <span class="yaml-dash">-</span>name: All the plugins
#### command: ls ansible/plugins/

- action
- cache
- **callback**
- connection
- filter
- lookup
- shell
- strategy
- terminal
- test
- vars

- modules
- module_utils
- module_doc_fragments


+++

### <span class="yaml-dash">-</span>name: CallbackBase
#### debug:<br/>&nbsp;&nbsp;var: ansible.plugins.callback.CallbackBase

```python
class CallbackBase:

    CALLBACK_VERSION: '2.0'
    CALLBACK_TYPE: 'stdout'
    CALLBACK_NAME: 'myplugin'
    CALLBACK_NEEDS_WHITELIST: True

```
+++

### <span class="yaml-dash">-</span>name: CALLBACK_TYPE
#### debug:<br/>&nbsp;&nbsp;var: CallbackBase.CALLBACK_TYPE

- `stdout`: Only one
- `notification`: 
- `aggregate`

+++

### <span class="yaml-dash">-</span>name: Loaded when
#### debug: var=run_when

+++

### <span class="yaml-dash">-</span>name: Batteries Included
#### command: ls ansible/plugins/callback/*.py

- Default Stdout  <!-- .element: class="fragment " -->
    - `default` (`ansible_playbook`)
    - `minimal` (`ansible`)
- Other Stdout <!-- .element: class="fragment fade-up" -->
    - `actionable`
    - `debug`
    - `dense`
    - `json`
    - ...
- Notification <!-- .element: class="fragment" -->
    - `context_demo`
- Aggregagte <!-- .element: class="fragment" -->

+++


### <span class="yaml-dash">-</span>name: Bring Your Own
#### set_fact:

        where: '{{role_dir}}/callback_plugins'
        where: '{{playbook_dir}}/callback_plugins'
        

---

### <span class="yaml-dash">-</span>name: Playbooks, Plays & Tasks
#### hosts: Callback Plugin Demo
#### tasks: ...

+++

### <span class="yaml-dash">-</span>name: Once Per Playbook
#### `debug: var=v2_playbook_on_start`

```python
    def v2_playbook_on_start(self, playbook):
        filename = getattr(playbook, '_file_name', '???')
```

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

### <span class="yaml-dash">-</span>name: Never Used
#### debug: var={{item}}<br/>when: false<br/>`with_items`:<br/>&nbsp;&nbsp;-&nbsp;`v2_on_file_diff`<br/>&nbsp;&nbsp;-&nbsp;`v2_runner_on_no_hosts`

---

### <span class="yaml-dash">-</span>name: What About...
#### hosts: Callback Plugin Demo
#### tasks: ...

+++

### <span class="yaml-dash">-</span>name: Capturing Stdout

+++

<img src="./assets/md/assets/img/no-log.gif" class="meme"/>


### <span class="yaml-dash">-</span>name: My ⨍µ¢₭ℹ︎ℵ§ Passwords


---

### <span class="yaml-dash">-</span>name: And Then
#### hosts: You
#### tasks: ...
