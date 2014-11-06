#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Admin
  

Copyright 2014 Li Yun <leven.cn@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import unittest


class AdminError(Exception):
    '''Base exception for admin module.
    '''
    def __init__(self, e=None, msg=''):
        self._error = e
        self._msg = msg

    
    def __str__(self):
        if self._error:
            return str(self._error)
        elif len(self._msg) != 0:
            return self._msg
        else:
            return 'Unknown Error'
        

class AdminTest(unittest.TestCase):
    '''Unit testing for admin module.
    '''
    def test_AdminError(self):
        with self.assertRaises(AdminError):
            raise AdminError()
            
            
if __name__ == '__main__':
    unittest.main()

    # Check system
    import platform
    import sys
    if platform.system != 'Linux':
        sys.exit('NOT Linux!')

    # Initialization
    import subprocess
    linux_dist = platform.linux_distribution()
    if linux_dist[0] == 'Ubuntu':
        linux_dist_version = linux_dist[1]
        if float(linux_dist_version) == 12.04:
            # Install PIP 3
            subprocess.check_call('sudo apt-get install python3-setuptools')
            subprocess.check_call('sudo easy_install3 -m pip')
        elif float(linux_dist_version) == 14.04:
            # Install PIP 3
            subprocess.check_call('sudo apt-get install python3-dev python3-pip')

