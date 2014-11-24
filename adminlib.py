#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Admin Library


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
import sys
import unittest


if sys.version_info.major != 3 or sys.version_info.minor < 1:
    sys.exit('Python 3.2+ required')


class AdminError(Exception):
    '''Base exception for admin module.
    '''
    def __init__(self, err=None, msg=''):
        if err is not None and len(msg) != 0:
            self._error = err(msg)
        else:
            self._error = err
        self._msg = msg


    def __str__(self):
        if self._error is not None:
            return str(self._error)
        elif len(self._msg) != 0:
            return self._msg
        else:
            return 'Unknown Error'


def shell(cmd):
    '''Run shell command without output.

    @param cmd shell command
    @exception AdminError(subprocess.CalledProcessError) - shell command error

    @warning NOT supported on Windows
    '''
    try:
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError as err:
        raise AdminError(err=err)


def shell_output(cmd) -> str:
    '''Run shell command with output.

    @param cmd shell command
    @return shell output without ending newline
    @exception AdminError(subprocess.CalledProcessError) - shell command error

    @warning NOT supported on Windows
    '''
    try:
        output = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError as err:
        raise AdminError(err=err)
    return output.strip().decode()


class AdminTest(unittest.TestCase):
    '''Unit testing for admin module.
    '''
    def setUp(self):
        # Initialization
        pass


    def tearDown(self):
        # Clean up
        pass


    def test_AdminError(self):
        with self.assertRaises(AdminError):
            raise AdminError()

        with self.assertRaises(AdminError) as err:
            raise AdminError()
        self.assertTrue(isinstance(err.exception, AdminError))
        self.assertEqual(str(err.exception), 'Unknown Error')

        with self.assertRaises(AdminError) as err:
            raise AdminError(err=KeyError, msg='KeyError Message')
        self.assertEqual(str(err.exception), "'KeyError Message'")

        with self.assertRaises(AdminError) as err:
            raise AdminError(msg='CustomError Message')
        self.assertEqual(str(err.exception), 'CustomError Message')


    @unittest.skipIf(sys.platform == 'win32', 'not supported on Windows')
    def test_shell(self):
        # Since `shell()` is a thin wrapper for standard API: `subprocess.check_call()`,
        # it needs to test exception raising only.
        with self.assertRaises(AdminError) as err:
            shell('not-exist-command')
        self.assertTrue(isinstance(err.exception._error, subprocess.CalledProcessError))


    @unittest.skipIf(sys.platform == 'win32', 'not supported on Windows')
    def test_shell_output(self):
        # Since `shell_output()` is a thin wrapper for standard API: `subprocess.check_output()`,
        # it needs to test exception raising only.
        if sys.platform == 'darwin':
            self.assertTrue(shell_output('python3.{0} --version'.format(sys.version_info.minor)).startswith('Python'))
        else:
            self.assertTrue(shell_output('python3 --version').startswith('Python'))

        with self.assertRaises(AdminError) as err:
            self.assertTrue(shell_output('not-exist-command').startswith('anything'))
        self.assertTrue(isinstance(err.exception._error, subprocess.CalledProcessError))


if __name__ == '__main__':
    if sys.platform == 'win32':
        # On Windows, IDLE would show trace-back output of SystemExit exception.
        unittest.main(exit=False)
    else:
        unittest.main()
