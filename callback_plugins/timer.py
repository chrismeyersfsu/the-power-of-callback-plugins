# Python
from __future__ import (absolute_import, division, print_function)

# Ansible
from ansible.plugins.callback.timer import CallbackModule as CallbackModule_timer


class CallbackModule(CallbackModule_timer):
    '''
    Custom timer callback module subclass to show loading from playbook directory.
    '''

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'timer'
    CALLBACK_NEEDS_WHITELIST = True

    def __init__(self):
        super(CallbackModule, self).__init__()
        print("loaded timer from '{{playbook_dir}}/callback_plugins'")
