# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='caption',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
