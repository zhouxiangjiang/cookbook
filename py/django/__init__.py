#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package py
Django Cookbook

  - Getting Started
  

## Getting Started

```bash
# Static files
# Add STATIC_ROOT of <site-name>/settings.py
python3 manage.py collectstatic

# Create App
python3 manage.py startapp <app-name>
# Add <app-name> into INSTALLED_APPS of <site-name>/settings.py
python3 manage.py makemigrations <app-name>

# Django Shell
python3 manage.py shell

# Django Admin User
python3 manage.py createsuperuser

# Update Models
python3 manage.py makemigrations <app-name>
python3 manage.py migrate

# Testing
python3 manage.py runserver <ip>:<port>
```

## References

  - [Python 3 Documentation](https://docs.python.org/3/)
  - [Django](https://www.djangoproject.com/)
  
      
Copyright (c) 2014 Li Yun <leven.cn@gmail.com>
All Rights Reserved.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
'''

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        import subprocess
        import os
        
        if sys.argv[1] == 'init':
            # Install Django
            subprocess.check_call('sudo pip3 install --upgrade django',
                    shell=True)
                    
        else:
            # Create a Django project
            project_name = sys.argv[1]
            subprocess.check_call('django-admin startproject ' + project_name,
                    shell=True)
            os.chdir(project_name)
            subprocess.check_call('python3 manage.py migrate', shell=True)
    
    print('Hello Django!')
