# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0002_auto_20170211_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
