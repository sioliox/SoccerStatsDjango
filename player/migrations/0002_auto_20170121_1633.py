# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.URLField(max_length=255, null=True),
        ),
    ]
