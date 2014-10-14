#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package py
Django Cookbook

  - Getting Started
  - App
  

## Getting Started

```bash
# Static files
# Add STATIC_ROOT of <site-name>/settings.py
python3 manage.py collectstatic

# Create App
python3 manage.py startapp <app-name>
# Add <app-name> into INSTALLED_APPS of <site-name>/settings.py

# Django Shell
python3 manage.py shell

# Django Admin User
python3 manage.py createsuperuser

# Testing Server
python3 manage.py runserver <ip>:<port>
```

## App

**STEP 1**: Update models in `<app-name>/models.py`

```bash
python3 manage.py makemigrations <app-name>
python3 manage.py migrate
```

**STEP 2**: Update views in `<app-name>/views.py`

**STEP 3**: Map views to URLs in `<app-name>/urls.py` and `<site-name>/urls.py`

## References

  - [Django](https://www.djangoproject.com/)
  - [Django 1.7 Documentation](https://docs.djangoproject.com/en/1.7/)
  - [Django 1.7 API Reference](https://docs.djangoproject.com/en/1.7/ref/)
  
      
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
            django_version = subprocess.check_output('django-admin version',
                    shell=True)
            print('Django {0}'.format(django_version.strip().decode()))
                    
        else:
            # Create a Django project
            project_name = sys.argv[1]
            subprocess.check_call('django-admin startproject ' + project_name,
                    shell=True)
            os.chdir(project_name)
            subprocess.check_call('python3 manage.py migrate', shell=True)
    else:
        print('Hello Django!')
    
