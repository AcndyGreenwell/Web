# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0015_auto_20160329_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='options',
        ),
        migrations.AddField(
            model_name='timetable',
            name='options',
            field=models.ManyToManyField(help_text='Набор настроек', null=True, to='counter.ZoneOption'),
        ),
    ]
