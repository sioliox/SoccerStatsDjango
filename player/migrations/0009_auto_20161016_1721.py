# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-16 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0008_auto_20161016_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(null=True, upload_to='.'),
        ),
    ]