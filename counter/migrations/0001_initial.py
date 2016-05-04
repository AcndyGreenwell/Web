# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cameras',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.TextField()),
                ('direcrition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ZoneOptions',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('camera', models.ForeignKey(to='counter.Cameras')),
                ('directions', models.ForeignKey(to='counter.Directions')),
            ],
        ),
        migrations.AddField(
            model_name='zoneoptions',
            name='zone',
            field=models.ForeignKey(to='counter.Zones'),
        ),
    ]
