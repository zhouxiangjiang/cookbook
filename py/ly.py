#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''My Python.
  

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

import subprocess
        

## Run shell command without output.
#
# @param cmd shell command
# @exception LyError(subprocess.CalledProcessError) - shell command error
def shell(cmd):
    try:
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError as err:
        raise LyError(err)
    
   
## Run shell command with output.
#
# @param cmd shell command
# @return shell output without ending newline
# @exception LyError(subprocess.CalledProcessError) - shell command error   
def shell_output(cmd) -> str:
    try:
        output = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError as err:
        raise LyError(err)
    return output.strip().decode()
    
    
if __name__ == '__main__':
    assert shell_output('python3 --version').startswith('Python')