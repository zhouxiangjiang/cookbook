#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Setup cookbook environment on OS X or Linux.


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

import admin


def setup():
    '''Setup.'''
    sys_type = platform.system()
    if sys_type == 'Linux':

        # Determine Linux distribution
        dist = platform.linux_distribution()
        dist_type = dist[0]
        dist_version = float(dist[1])

        if dist_type == 'Ubuntu':
            admin.shell('sudo apt-get install nginx')
            if version == 12.04:
                # Issue: Cannot install python3-setuptools on Ubuntu 12.04.5
                admin.shell('sudo apt-get install python3-setuptools')
                admin.shell('sudo easy_install3 -m pip')
            elif version == 14.04:
                admin.shell('sudo apt-get install python3-dev python3-pip')
            admin.shell('sudo pip3 install --upgrade django')
    elif sys_type == 'Darwin':  # OS X
        admin.shell('sudo port install nginx py34-pip')
        admin.shell('sudo pip-3.4 install --upgrade django')
    else:
        sys.exit('Current system: {0}, NOT supported!'.format(sys_type))


if __name__ == '__main__':
    setup()

