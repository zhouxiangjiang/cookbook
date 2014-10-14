# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=128)),
                ('num', models.PositiveIntegerField(default=1)),
                ('unit', models.CharField(max_length=16)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('date', models.DateTimeField()),
                ('user', models.ForeignKey(to='vip.VIPUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='vipuser',
            name='bluetooth_mac',
            field=models.CharField(default='00:00:00:00:00:00', max_length=17),
            preserve_default=True,
        ),
    ]
