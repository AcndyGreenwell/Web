# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 08:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0023_auto_20160404_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
