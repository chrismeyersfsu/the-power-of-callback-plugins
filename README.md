# The Power of Callback Plugins

*To be presented at [AnsibleFest San Francisco 2017](https://www.ansible.com/ansiblefest).*

Ansible callback plugins provide the essential hook for capturing the results of
a Playbook run, beyond what can be obtained from only logging stdout. As the
primary author of the callback plugin used in Tower, I'll present detailed
knowledge of the callback hooks available and how they can be used for reporting
and statistics associated with Playbook runs.

In this session, you will learn:

* How to write a callback plugin for Ansible
* The available callback functions and parameters
* What can be accomplished with the plugins included within Ansible
* How Tower uses callback plugins to capture the output of job runs
* Gotchas you might encounter along the way

<span>&nbsp;</span>

<!-- <img style="float: left; border-radius: 100%; margin: 0 1em 0 0;" src="https://www.ansible.com/hs-fs/hubfs/2016_Images/AnsibleFestNY16/Chris-Church.jpg?t=1503065851248&width=140&height=140&name=Chris-Church.jpg"/> -->

**Chris Church**, Software Design Engineer, Ansible by Red Hat

<a href="https://twitter.com/flyingfred0"><img src="https://www.ansible.com/hubfs/-2015-template-assets/images/team/team-twitter.png?t=1503065851248"/></a>
<a href="https://www.linkedin.com/in/flyingfred0"><img src="https://www.ansible.com/hubfs/-2015-template-assets/images/team/team-linkedin.png?t=1503065851248"/></a>
