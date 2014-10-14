# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0002_auto_20141014_0627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vipuser',
            old_name='bluetooth_mac',
            new_name='bluetooth_addr',
        ),
    ]
