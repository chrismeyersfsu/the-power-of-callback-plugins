<!-- .element: class="x" -->
<pre style="box-shadow: none; font-weight: bold;">
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
#### tasks: ...  <!-- .element: class="fragment" -->


Note:
Do a happy dance here.

+++

### <span class="yaml-dash">-</span>name: Who Dis?
#### set_fact:
#### &nbsp;&nbsp;`tower_api_developer: Since March 2013`  <!-- .element: class="fragment" -->
#### &nbsp;&nbsp;`tower_callback_plugin: ~90% of current implementation`  <!-- .element: class="fragment" -->
<!-- https://github.com/ansible/awx/blob/a61a3538291812de5032bc383e662c000e33741e/lib/plugins/callback/acom_callback.py -->
#### &nbsp;&nbsp;`ansible_sign: github.com/cchurch/ansible-sign`  <!-- .element: class="fragment" -->
#### &nbsp;&nbsp;`ansible_winning: github.com/cchurch/ansible-winning`  <!-- .element: class="fragment" -->

Note:

---

### <span class="yaml-dash">-</span>name: How Tower Runs a Job
#### hosts: Ansible Tower
#### tasks: ...

Note:

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

### <span class="yaml-dash">-</span>name: Job Templates API
#### `get_url: url=tower/api/v1/job_templates/242/`

<!-- <iframe src="https://tower.testing.ansible.com/" width="400" height="300">FIXME</iframe> -->

+++

### <span class="yaml-dash">-</span>name: Job Templates UI
#### `get_url: url=tower/#/templates/job_template/242`

+++

### <span class="yaml-dash">-</span>name: Launch a Job
#### `get_url: url=tower/#/jobs/17673`

+++

### <span class="yaml-dash">-</span>name: Job API
#### `get_url: url=tower/api/v1/jobs/17673`

+++

### <span class="yaml-dash">-</span>name: Job Events API
#### `get_url: url=tower/api/v1/jobs/17673/job_events/`

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
#### debug: var=ansible.plugins.callback.CallbackBase

```python
class CallbackBase:

    CALLBACK_VERSION: '2.0'
    CALLBACK_TYPE: 'stdout'
    CALLBACK_NAME: 'myplugin'
    CALLBACK_NEEDS_WHITELIST: True

```
+++

### <span class="yaml-dash">-</span>name: CALLBACK_TYPE
#### debug: var=CallbackBase.CALLBACK_TYPE

- `stdout`: Only one
- `notification`: 
- `aggregate`

+++

### <span class="yaml-dash">-</span>name: Loaded when
#### debug: var=run_when

+++

### <span class="yaml-dash">-</span>name: Batteries Included
#### command: ls ansible/plugins/callback/*.py

- Default Stdout
    - `default` (`ansible_playbook`)
    - `minimal` (`ansible`)
- Other Stdout <!-- .element: class="fragment" -->
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

