# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0007_auto_20160318_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='camera',
            field=models.ForeignKey(help_text='Камера', on_delete=django.db.models.deletion.CASCADE, to='counter.Camera'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='directions',
            field=models.ForeignKey(default=1, help_text='Направление', on_delete=django.db.models.deletion.CASCADE, to='counter.Direction'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='height',
            field=models.IntegerField(help_text='Высота'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='name',
            field=models.CharField(help_text='Имя', max_length=200),
        ),
        migrations.AlterField(
            model_name='zone',
            name='width',
            field=models.IntegerField(help_text='Ширина'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='x1',
            field=models.IntegerField(help_text='x1'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='x2',
            field=models.IntegerField(help_text='x2'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='x3',
            field=models.IntegerField(help_text='x3'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='x4',
            field=models.IntegerField(help_text='x4'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='y1',
            field=models.IntegerField(help_text='y1'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='y2',
            field=models.IntegerField(help_text='y2'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='y3',
            field=models.IntegerField(help_text='y3'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='y4',
            field=models.IntegerField(help_text='y4'),
        ),
    ]
