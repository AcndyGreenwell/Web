# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 03:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('counter', '0020_auto_20160404_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camera',
            name='user',
        ),
        migrations.AddField(
            model_name='camera',
            name='group',
            field=models.ManyToManyField(to='auth.Group'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zone',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
            preserve_default=False,
        ),
    ]