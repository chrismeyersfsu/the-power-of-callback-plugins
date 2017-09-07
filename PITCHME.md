<!-- .element: class="x" -->

<img src="./assets/gifs/callback-boy.gif" class="meme"/>


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

<img src="./assets/gifs/who-dis.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: Who Dis?
#### set_fact:
#### <!-- .element: class="fragment" -->&nbsp;&nbsp;`tower_api_developer`: > <br/> &nbsp;&nbsp;&nbsp;&nbsp;[Since March 2013](https://github.com/ansible/awx/commit/a61a3538291812de5032bc383e662c000e33741e)
#### <!-- .element: class="fragment" -->&nbsp;&nbsp;`tower_callback_plugin`: > <br/> &nbsp;&nbsp;&nbsp;&nbsp;[~90% of current implementation](https://github.com/ansible/awx/blame/c7a85d9738a1e7ddd52a65968766800ed8c34d12/awx/lib/tower_display_callback/module.py)
#### <!-- .element: class="fragment" -->&nbsp;&nbsp;`ansible_winning: >` <br/> &nbsp;&nbsp;&nbsp;&nbsp;[github.com/cchurch/ansible-winning](https://github.com/cchurch/ansible-winning)
#### <!-- .element: class="fragment" --><img src="./assets/gifs/ansible-sign.gif" style="position: absolute; top: 145px; right: -35px; clip: rect(45px,230px,235px,35px);"/>&nbsp;&nbsp;`ansible_sign: >` <br/> &nbsp;&nbsp;&nbsp;&nbsp;[github.com/cchurch/ansible-sign](https://github.com/cchurch/ansible-sign)

Note:

---

<img src="./assets/gifs/what-is.gif" class="meme" style="top: 100px;"/>

### <span class="yaml-dash">-</span>name: What *IS* a Callback Plugin?
#### hosts: Ansible Core
#### tasks: ...

+++

<img src="./assets/gifs/plugins.gif" class="meme"/>

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

<img src="./assets/gifs/callback-base.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: CallbackBase
#### debug:<br/>&nbsp;&nbsp;var: ansible.plugins.callback.CallbackBase

<pre class="fragment"><code class="python hljs">class CallbackBase:

    CALLBACK_VERSION = '2.0'
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'myplugin'
    CALLBACK_NEEDS_WHITELIST = True

</code><code class="fragment python hljs">    def v2_on_any(self, *args, **kwargs):
        pass
</code></pre>

+++

<img src="./assets/gifs/callback-type.gif" class="meme"/>

### <span class="yaml-dash">-</span>name: CALLBACK_TYPE
#### debug:<br/>&nbsp;&nbsp;var: CallbackBase.CALLBACK_TYPE

<ul class="fragment" style="margin-top: 1em;">
  <li><b>stdout</b>: Only one</li>
  <li><b>notification</b>: Zero or more, may be whitelisted</li>
  <li><b>aggregate</b>: Zero or more, may be whitelisted</li>
</ul>

+++

<div><img src="./assets/gifs/built-in.gif" class="meme"/></div>

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

<div><img src="./assets/gifs/bring-your-own.gif" class="meme"/></div>

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

<div><img src="./assets/gifs/loaded-when.gif" class="meme"/></div>

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

<div><img src="./assets/gifs/playbooks-plays-tasks.gif" class="meme" style="top: 100px;"/></div>

### <span class="yaml-dash">-</span>name: Playbooks, Plays & Tasks
#### hosts: Demo Callback Plugin
#### tasks: ...

+++

<div><img src="./assets/gifs/playbook-start.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Per Playbook
#### `debug: var=v2_playbook_on_start`

<div class="fragment" style="margin-top: 1em;">
<pre><code class="python">def v2_playbook_on_start(self, playbook):
    self.playbook = playbook
    filename = getattr(playbook, '_file_name', '???')
    plays = playbook.get_plays()
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=playbook</h4>
<pre><code class="nohighlight">&lt;ansible.playbook.Playbook object&gt;
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=playbook_stdout (-vv)</h4>
<pre><code class="nohighlight">PLAYBOOK: demo.yml &#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;
1 plays in demo.yml
</code></pre>
</div>

+++

<div><img src="./assets/gifs/playbook-on-vars-prompt.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Prompts
#### debug: ><br/>&nbsp;&nbsp;var=`v2_playbook_on_vars_prompt`

<div class="fragment">
<pre><code class="python">def v2_playbook_on_vars_prompt(self,
                               varname,
                               private=True,
                               prompt=None,
                               encrypt=None,
                               confirm=False,
                               salt_size=None,
                               salt=None,
                               default=None):
    pass
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>set_fact:<br/>&nbsp;&nbsp;called_before: display.do_var_prompt<br/>&nbsp;&nbsp;return_value: ignored<br/>&nbsp;&nbsp;override_possible: not really</h4>
</div>

+++

<div><img src="./assets/gifs/playbook-include.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Includes<sup>*</sup>
#### debug: var=v2_playbook_on_include

<div class="fragment" style="margin-top: 1.1em;">
<pre><code class="python">def v2_playbook_on_include(self, included_file):
    filename = included_file._filename
    args = included_file._args
    task = included_file._task
    hosts = included_file._hosts
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=included_file</h4>
<pre><code class="nohighlight">&lt;ansible.playbook.IncludedFile object&gt;
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=include_stdout</h4>
<pre><code class="nohighlight">included: file.yml for host</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>set_fact: actually_called=rarely<sup>*</sup></h4>
</div>

+++

<div><img src="./assets/gifs/playbook-play.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Per Play
#### debug: ><br/>&nbsp;&nbsp;var=v2_playbook_on_play_start

<div class="fragment">
<pre><code class="python">def v2_playbook_on_play_start(self, play):
    playbook = self.playbook
    self.play = play
    if isinstance(play.hosts, list):
        pattern = ','.join(play.hosts)
    else:
        pattern = play.hosts
    name = play.get_name().strip() or pattern
    uuid = str(play._uuid)
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=play</h4>
<pre><code class="nohighlight">&lt;ansible.playbook.Play object&gt;
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=play_stdout</h4>
<pre><code class="nohighlight">PLAY [my play] &#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;</code></pre>
</div>

+++

<div><img src="./assets/gifs/playbook-task.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Per Task
#### debug: ><br/>&nbsp;&nbsp;var=v2_playbook_on_task_start

<div class="fragment">
<pre><code class="python">def v2_playbook_on_task_start(self, task, is_conditional):
    playbook, play = self.playbook, self.play
    self.task = task
    name, action = task.name or task.get_name(), task.action
    path = task.get_path()
    no_log = task.no_log
    role = task._role._role_name if task._role else None
    uuid = str(task._uuid)
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=task</h4>
<pre><code class="nohighlight">&lt;ansible.playbook.Task object&gt;
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=task_stdout (-vv)</h4>
<pre><code class="nohighlight">TASK [my task] &#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;
task path: demo.yml:9</code></pre>
</div>

+++

<div><img src="./assets/gifs/playbook-handler.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Handlers
#### debug: ><br/>&nbsp;&nbsp;var=`v2_playbook_on_handler_task_start`

<div class="fragment">
<pre><code class="python">def v2_playbook_on_handler_task_start(self, task):
    self.v2_playbook_on_task_start(task, is_conditional=True)
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=handler_task_stdout (-vv)</h4>
<pre><code class="nohighlight">RUNNING HANDLER [my handler] &#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;</code></pre>
</div>

+++

<div><img src="./assets/gifs/no-hosts-matched.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: No Hosts Matched
#### debug: ><br/><br/>&nbsp;&nbsp;var=`v2_playbook_on_no_hosts_matched`

<div class="fragment">
<pre><code class="python">def v2_playbook_on_no_hosts_matched(self):
    playbook, play = self.playbook, self.play
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=no_hosts_matched_stdout</h4>
<pre><code class="nohighlight">skipping: no hosts matched</code></pre>
</div>

+++

<div><img src="./assets/gifs/no-hosts-remaining.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: No Hosts Remaining
#### debug: ><br/>&nbsp;&nbsp;var=v2_playbook_on_no_hosts_remaining

<div class="fragment">
<pre><code class="python">def v2_playbook_on_no_hosts_remaining(self):
    playbook, play = self.playbook, self.play
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=no_hosts_remaining_stdout</h4>
<pre><code class="nohighlight">NO MORE HOSTS LEFT &#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;</code></pre>
</div>

+++

<div><img src="./assets/gifs/playbook-stats.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Stats
#### debug: var=v2_playbook_on_stats

<div class="fragment" style="margin-top: 1em;">
<pre><code class="python">def v2_playbook_on_stats(self, stats):
    playbook = self.playbook
    changed = stats.changed
    dark = stats.dark
    failures = stats.failures
    ok = stats.ok
    processed = stats.processed
    skipped = stats.skipped
    custom = getattr(stats, 'custom', {})
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=stats.ok</h4>
<pre><code class="python">{'host': 22}
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=stats_stdout</h4>
<pre><code class="nohighlight">PLAY RECAP &#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;
host    : ok=22    changed=4    unreachable=0    failed=0
</code></pre>
</div>

+++

<div><img src="./assets/gifs/playbook-never.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Never Called
#### debug: var={{item}}<br/>when: false<br/>`with_items`:<br/>&nbsp;&nbsp;-&nbsp;`v2_playbook_on_notify`<br/>&nbsp;&nbsp;-&nbsp;`v2_playbook_on_cleanup_task_start`

---

<div><img src="./assets/gifs/runner-events.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Runner Events
#### hosts: Demo Callback Plugin
#### tasks: ...

+++

<div><img src="./assets/gifs/runner-ok.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: OK
#### debug: var=`v2_runner_on_ok`

<div class="fragment">
<pre><code class="python">def v2_runner_on_ok(self, result):
    playbook, play, task = self.playbook, self.play, self.task
    host = result._host
    hostname = result._host.get_name()
    remote_addr = result._host.address
    res = result._result
    event_loop = result._task.loop if hasattr(result._task, 'loop') else None
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=ok_stdout (-vv)</h4>
<pre><code class="nohighlight">ok: [host] => {"changed": false, "cmd": ["uptime"], "delta": "0:00:00.011449", "end": "2017-09-07 02:43:31.610607", "rc": 0, "start": "2017-09-07 02:43:31.599158", "stderr": "", "stderr_lines": [], "stdout": " 2:43  up 5 days, 11:19, 7 users, load averages: 1.98 1.89 1.94", "stdout_lines": [" 2:43  up 5 days, 11:19, 7 users, load averages: 1.98 1.89 1.94"]}
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=ok_task</h4>
<pre><code class="yaml">- command: uptime
  changed_when: false
</code></pre>
</div>

+++

<div><img src="./assets/gifs/runner-ok.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: OK
#### debug: var=`result`

<div class="fragment">
<pre><code class="nohighlight">&lt;ansible.executor.task_result.TaskResult object&gt;</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=result._result</h4>
<pre><code class="json">{
    "_ansible_no_log": false,
    "_ansible_parsed": true,
    "changed": false,
    "cmd": [
        "uptime"
    ],
    "delta": "0:00:00.014762",
    "end": "2017-09-07 02:53:26.721913",
    "invocation": {
        "module_args": {
            "_raw_params": "uptime",
            "_uses_shell": false,
            "chdir": null,
            "creates": null,
            "executable": null,
            "removes": null,
            "warn": true
        }
    },
    "rc": 0,
    "start": "2017-09-07 02:53:26.707151",
    "stderr": "",
    "stderr_lines": [],
    "stdout": " 2:53  up 5 days, 11:29, 7 users, load averages: 2.33 2.33 2.15",
    "stdout_lines": [
        " 2:53  up 5 days, 11:29, 7 users, load averages: 2.33 2.33 2.15"
    ]
}
</code></pre>
</div>

+++

<div><img src="./assets/gifs/runner-failed.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Failed
#### debug: var=`v2_runner_on_failed`

<div class="fragment" style="margin-top: 1em;">
<pre><code class="python">def v2_runner_on_failed(self, result, ignore_errors=False):
    playbook, play, task = self.playbook, self.play, self.task
    ...
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=failed_stdout (-vv)</h4>
<pre><code class="nohighlight">fatal: [me]: FAILED! => {"changed": false, "failed": true, "failed_when_result": true, "ping": "pong"}
...ignoring
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=failed_task</h4>
<pre><code class="yaml">- action: ping
  failed_when: true
  ignore_errors: true
</code></pre>
</div>

+++

<div><img src="./assets/gifs/runner-skipped.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Skipped
#### debug: var=`v2_runner_on_skipped`

<div class="fragment">
<pre><code class="python">def v2_runner_on_skipped(self, result):
    playbook, play, task = self.playbook, self.play, self.task
    skip_reason = result._result.get('skip_reason')
    ...
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=skipped_stdout (-vv)</h4>
<pre><code class="nohighlight">skipping: [host] => {"changed": false, "skip_reason": "Conditional result was False", "skipped": true}
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=skipped_task</h4>
<pre><code class="yaml">- action: ping
  when: false
</code></pre>
</div>

+++

<div><img src="./assets/gifs/runner-unreachable.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Unreachable
#### debug: var=`v2_runner_on_unreachable`

<div class="fragment">
<pre><code class="python">def v2_runner_on_unreachable(self, result):
    playbook, play, task = self.playbook, self.play, self.task
    msg = result._result.get('msg')
    ...
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=skipped_stdout (-vv)</h4>
<pre><code class="nohighlight">fatal: [host]: UNREACHABLE! => {"changed": false, "msg": "Failed to connect to the host via ssh: ssh: connect to host 127.0.0.1 port 22: Connection refused\r\n", "unreachable": true}
</code></pre>
</div>

+++

<div><img src="./assets/gifs/runner-item-ok.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Item OK
#### debug: var=`v2_runner_item_on_ok`

<div class="fragment">
<pre><code class="python">def v2_runner_item_on_ok(self, result):
    playbook, play, task = self.playbook, self.play, self.task
    item = result._result.get('item')
    ...
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=item_ok_stdout (-vv)</h4>
<pre><code class="nohighlight">changed: [host] => (item=True) => {"changed": true, "cmd": ["echo", "True"], "delta": "0:00:00.009627", "end": "2017-09-07 09:01:25.905027", "item": true, "rc": 0, "start": "2017-09-07 09:01:25.895400", "stderr": "", "stderr_lines": [], "stdout": "True", "stdout_lines": ["True"]}
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=item_ok_task</h4>
<pre><code class="yaml">- debug: msg='{{item}}'
  with_items: [one, two, three]
</code></pre>
</div>

+++

<div><img src="./assets/gifs/runner-item-failed.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Item Failed
#### debug: var=`v2_runner_item_on_failed`

<div class="fragment" style="margin-top: 1em;">
<pre><code class="python">def v2_runner_item_on_failed(self, result):
    playbook, play, task = self.playbook, self.play, self.task
    item = result._result.get('item')
    ...
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=item_failed_stdout (-vv)</h4>
<pre><code class="nohighlight">failed: [host] (item=one) => {"failed": true, "failed_when_result": true, "item": "one", "msg": "one"}
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=item_failed_task</h4>
<pre><code class="yaml">- debug: msg='{{item}}'
  with_items: [one, two, three]
  failed_when: true
  ignore_errors: true
</code></pre>
</div>

+++

<div><img src="./assets/gifs/runner-item-skipped.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Item Skipped
#### debug: var=`v2_runner_item_on_skipped`

<div class="fragment" style="margin-top: 1em;">
<pre><code class="python">def v2_runner_item_on_skipped(self, result):
    playbook, play, task = self.playbook, self.play, self.task
    item = result._result.get('item')
    ...
</code></pre>
<div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=item_skipped_stdout (-vv)</h4>
<pre><code class="nohighlight">skipping: [host] => (item=one) => {"changed": false, "item": "one", "skip_reason": "Conditional result was False", "skipped": true}
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=item_skipped_task</h4>
<pre><code class="yaml">- debug: msg='{{item}}'
  with_items: [one, two, three]
  when: false
</code></pre>
</div>

+++

<div><img src="./assets/gifs/file-diff.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: File Diff
#### debug: var=`v2_on_file_diff`

<div class="fragment">
<pre><code class="python">def v2_on_file_diff(self, result):
    playbook, play, task = self.playbook, self.play, self.task
    diff = result._result.get('diff') or {}
    before_header = diff.get('before_header', '')
    before = diff.get('before', '')
    after_header = diff.get('after_header', '')
    after = diff.get('after', '')
    ...
</code></pre>
<div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=diff_stdout (-vv)</h4>
<pre><code class="nohighlight">--- before: /tmp/myself
+++ after: /var/folders/d9/6l0j02nx09g5h05pjgbphvqh0000gn/T/tmpLzY3YX
@@ -1 +1 @@
-Thu Sep  7 09:59:50 PDT 2017
+Thu Sep  7 10:00:11 PDT 2017
</code></pre>
</div>

+++

<div><img src="./assets/gifs/file-diff.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: File Diff
#### debug: var=`diff_task`

<div class="fragment">
<pre><code class="yaml">- copy:
    content: '{{lookup("pipe", "date")}}'
    dest: '/tmp/{{inventory_hostname}}'
</code></pre>
</div>

<div class="fragment">
<p>--diff or ANSIBLE_DIFF_ALWAYS or ansible.cfg:</p>

<pre><code class="ini">[diff]
always=true
</code></pre>
</div>

+++

<div><img src="./assets/gifs/runner-retry.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Retry
#### debug: var=`v2_runner_on_retry`

<div class="fragment">
<pre><code class="python">def v2_runner_on_retry(self, result):
    playbook, play, task = self.playbook, self.play, self.task
    retries = result._result.get('retries')
    attempts = result._result.get('attempts')
    ...
</code></pre>
<div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=retry_stdout (-vv)</h4>
<pre><code class="nohighlight">FAILED - RETRYING: my task (99 retries left).
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=retry_task</h4>
<pre><code class="yaml">- shell: echo $(((RANDOM % 10) + 1))
  register: random_result
  until: random_result.stdout == "1"
  retries: 99
  delay: 1
</code></pre>
</div>

+++

<div><img src="./assets/gifs/runner-never.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Never Called
#### debug: var={{item}}<br/>when: false<br/>`with_items`:<br/>&nbsp;&nbsp;-&nbsp;`v2_runner_on_async_poll`<br/>&nbsp;&nbsp;-&nbsp;`v2_runner_on_async_ok`<br/>&nbsp;&nbsp;-&nbsp;`v2_runner_on_async_failed`<br/>&nbsp;&nbsp;-&nbsp;`v2_runner_on_file_diff`<br/>&nbsp;&nbsp;-&nbsp;`v2_runner_on_no_hosts`

---

<div><img src="./assets/gifs/what-about.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: What About?
#### hosts: Demo Callback Plugin
#### tasks: ...

+++

<div><img src="./assets/gifs/capture-stdout.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Capturing Stdout
#### debug: var=capture_event_data

<div class="fragment">
<pre><code class="python">with self.capture_event_data('v2_runner_on_ok', **event_data):
    super(CallbackModule, self).v2_runner_on_ok(result)
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=mark_begin</h4>
<pre><code class="python">def mark_begin(fileobj, event_uuid):
    b64data = base64.b64encode(json.dumps({'uuid': event_uuid}))
    fileobj.write(u'\x1b[K{}\x1b[{}D\x1b[K'.format(b64data, len(b64data)))
</code></pre>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=mark_end</h4>
<pre><code class="python">def mark_end(fileobj):
    b64data = base64.b64encode(json.dumps({}))
    fileobj.write(u'\x1b[K{}\x1b[{}D\x1b[K'.format(b64data, len(b64data)))
</code></pre>

+++

<div><img src="./assets/gifs/capture-stdout.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Capturing Stdout
#### debug: ><br/>&nbsp;&nbsp;var=ansible.utils.display.Display

<div class="fragment">
<pre><code class="python">class Display:

    def display(self, msg, color=None, stderr=False, screen_only=False, log_only=False):
        ...

    def verbose(self, msg, host=None, caplevel=2):
        ...

    def banner(self, msg, color=None, cows=True):
        ...
</code></pre>
</div>

+++

<div><img src="./assets/gifs/no-log.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: My ⨍®𝒾¢₭ℹ︎ℵ§ Passwords
#### debug: var=task.no_log

<div class="fragment" style="margin-top: 1em;">
<pre><code class="python">if task.no_log:
    task_args = 'NO LOG'
else:
    task_args = ', '.join(('%s=%s' % a for a in task.args.items()))
</code></pre>
</div>

<div class="fragment">
<h4><span class="yaml-dash">-</span>debug: var=_ansible_no_log</h4>
<pre><code class="python">if res.get('_ansible_no_log', False):
    res = {'censored': 'CENSORED'}
if res.get('results', []):
    res['results'] = copy(res['results'])
for i, item in enumerate(res.get('results', [])):
    if isinstance(item, dict) and item.get('_ansible_no_log', False):
        res['results'][i] = {'censored': 'CENSORED'}
</code></pre>

+++

<div><img src="./assets/gifs/callback-exceptions.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Callback Exceptions

<div class="fragment" style="margin-top: 4em;">
<p>ANSIBLE_DEBUG or ansible.cfg:</p>

<pre><code class="ini">[defaults]
debug=true
</code></pre>
</div>

---

<div><img src="./assets/gifs/tower-fall.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: How Tower Runs a Job
#### hosts: Ansible Tower
#### tasks: ...

+++

<div><img src="./assets/gifs/ansible-help.gif" class="meme"/></div>

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

<div><img src="./assets/gifs/templates-api.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Job Templates API
#### `get_url`: <br/>&nbsp;&nbsp;url: [tower/api/v1/job_templates/N/](https://tower/api/v1/job_templates/1/)

<iframe class="fragment" src="https://localhost:8043/api/v1/job_templates/5/"></iframe>

+++

<div><img src="./assets/gifs/templates-ui.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Job Templates UI
#### `get_url`: <br/>&nbsp;&nbsp;url: [tower/#/templates/job_template/N](https://tower/#/templates/job_template/1)

<iframe class="fragment" src="https://localhost:8043/#/templates/job_template/5"></iframe>

+++

<div><img src="./assets/gifs/launch-job.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Launch a Job
#### `get_url`: <br/>&nbsp;&nbsp;url: [tower/#/jobs/N](https://tower/#/jobs/1)

<iframe class="fragment" src="https://localhost:8043/#/templates?template_search=id__icontains_DEFAULT:5"></iframe>

+++

<div><img src="./assets/gifs/jobs-api.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Jobs API
#### `get_url`: <br/>&nbsp;&nbsp;url: [tower/api/v1/jobs/N/](https://tower/api/v1/jobs/1/)

<iframe class="fragment" src="https://localhost:8043/api/v1/jobs/?order_by=-id"></iframe>

+++

<div><img src="./assets/gifs/job-events-api.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: Job Events API
#### `get_url`: <br/>&nbsp;&nbsp;url: [tower/api/v1/jobs/N/job_events/](https://tower/api/v1/jobs/1/job_events/)

<iframe class="fragment" src="https://localhost:8043/api/v1/jobs/?order_by=-id"></iframe>

---

<div><img src="./assets/gifs/what-next.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: What Next?
#### hosts: You
#### tasks: ...

+++

<div><img src="./assets/gifs/potato.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: AWX
#### get_url:<br/>&nbsp;&nbsp;url: [github.com/ansible/awx](https://github.com/ansible/awx)

#### <!-- .element: class="fragment" --><span class="yaml-dash">-</span>set_fact:<br/>&nbsp;&nbsp;google_group: [awx-project](https://groups.google.com/d/forum/awx-project)<br/>&nbsp;&nbsp;freenode_irc: [ansible-awx](irc://irc.freenode.net/ansible-awx)

+++

<div><img src="./assets/gifs/fixme.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: FIXME
#### command: ><br>&nbsp;&nbsp;grep -hir fixme<br/>&nbsp;&nbsp;awx/lib/awx_display_callback/

<pre class="fragment" style="margin-top: 2em;"><code class="python"># FIXME: Task is "global" unless using free strategy!
# FIXME: Flag task path output as vv.
# FIXME: When this task UUID repeats, it means the play is using the free strategy...
# FIXME: Add count of plays/tasks.
# FIXME: Display detailed results or not based on verbosity.
# FIXME: Add verbosity for exception/results output.
</code></pre>

<div class="fragment">
<h4><span class="yaml-dash">-</span>set_fact: need_docs=true</h4>
<blockquote style="width: 90%;">"This is what callback plugins are for, sadly we are 'low on docs' on
this feature." @bcoca</blockquote>
</div>

+++

<div><img src="./assets/gifs/questions.gif" class="meme"/></div>

### <span class="yaml-dash">-</span>name: That's All!
#### pause:<br/>&nbsp;&nbsp;prompt: Any questions?

#### <!-- .element: class="fragment" --><span class="yaml-dash">-</span>set_fact:<br/>&nbsp;&nbsp;github: [@cchurch](https://github.com/cchurch)<br/>&nbsp;&nbsp;twitter: [@flyingfred0](https://twitter.com/flyingfred0)<br/>&nbsp;&nbsp;email: [cchurch@redhat.com](mailto:cchurch@redhat.com)
#### <!-- .element: class="fragment" --><span class="yaml-dash">-</span>get_url:<br/>&nbsp;&nbsp;url: [cchurch/the-power-of-callback-plugins](https://github.com/cchurch/the-power-of-callback-plugins)
