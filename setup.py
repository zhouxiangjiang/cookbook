#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Setup cookbook environment.
  

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

import platform
import sys
import subprocess


def setup():
    '''Setup.'''
    # Only support Linux
    sys_type = platform.system()
    if sys_type != 'Linux':
        sys.exit('Current system: {0}, NOT Linux!'.format(sys_type))

    # Shell tools
    def shell(cmd):
        subprocess.check_call(cmd, shell=True)

    # Install packages required
    linux_dist = platform.linux_distribution()
    if linux_dist[0] == 'Ubuntu':
        linux_dist_version = linux_dist[1]
        if float(linux_dist_version) == 12.04:
            # Install PIP 3
            shell('sudo apt-get install python3-setuptools')
            shell('sudo easy_install3 -m pip')
        elif float(linux_dist_version) == 14.04:
            # Install PIP 3
            shell('sudo apt-get install python3-dev python3-pip')

if __name__ == '__main__':
    setup()

