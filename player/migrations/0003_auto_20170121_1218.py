# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_auto_20170121_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='nationality',
            field=models.CharField(max_length=255),
        ),
    ]
