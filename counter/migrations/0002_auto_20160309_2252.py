# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('x1', models.IntegerField()),
                ('y1', models.IntegerField()),
                ('x2', models.IntegerField()),
                ('y2', models.IntegerField()),
                ('x3', models.IntegerField()),
                ('y3', models.IntegerField()),
                ('x4', models.IntegerField()),
                ('y4', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Cameras',
            new_name='Camera',
        ),
        migrations.RenameModel(
            old_name='Directions',
            new_name='Direction',
        ),
        migrations.RenameModel(
            old_name='ZoneOptions',
            new_name='ZoneOption',
        ),
        migrations.RemoveField(
            model_name='zones',
            name='camera',
        ),
        migrations.RemoveField(
            model_name='zones',
            name='directions',
        ),
        migrations.RenameField(
            model_name='camera',
            old_name='direcrition',
            new_name='direction',
        ),
        migrations.AlterField(
            model_name='zoneoption',
            name='zone',
            field=models.ForeignKey(to='counter.Zone'),
        ),
        migrations.DeleteModel(
            name='Zones',
        ),
        migrations.AddField(
            model_name='zone',
            name='camera',
            field=models.ForeignKey(to='counter.Camera'),
        ),
        migrations.AddField(
            model_name='zone',
            name='directions',
            field=models.ForeignKey(to='counter.Direction'),
        ),
    ]
