# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 07:47
from __future__ import unicode_literals

from django.db import migrations
import select_multiple_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0028_auto_20160421_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='days',
            field=select_multiple_field.models.SelectMultipleField(choices=[('MON', 'Понедельник'), ('TUE', 'Вторник'), ('WED', 'Среда'), ('THU', 'Четверг'), ('FRI', 'Пятница'), ('SUN', 'Суббота'), ('SAT', 'Воскресенье')], max_length=10, null=True),
        ),
    ]