# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-16 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_player_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='market_value_currency',
        ),
        migrations.AlterField(
            model_name='player',
            name='market_value',
            field=models.PositiveIntegerField(),
        ),
    ]
