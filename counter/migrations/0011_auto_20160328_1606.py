# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 09:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0010_auto_20160328_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optionsset',
            name='options',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='camera',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='options',
        ),
        migrations.DeleteModel(
            name='OptionsSet',
        ),
        migrations.DeleteModel(
            name='TimeTable',
        ),
    ]
