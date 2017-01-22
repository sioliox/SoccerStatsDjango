# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_auto_20170122_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('Keeper', 'Torwart'), ('Right-Back', 'Rechter Außenverteidiger'), ('Centre Back', 'Innenverteidiger'), ('Abwehr', 'Verteidiger'), ('Left-Back', 'Linker Außenverteidiger'), ('Defensive Midfield', 'Defensives Mittelfeld'), ('Left Midfield', 'Linkes Mittelfeld'), ('Central Midfield', 'Zentrales Mittelfeld'), ('Midfield', 'Mittelfeld'), ('Mittelfeld', 'Mittelfeld'), ('Right Midfield', 'Rechtes Mittelfeld'), ('Attacking Midfield', 'Offensives Mittelfeld'), ('Right Wing', 'Rechter Flügel'), ('Secondary Striker', 'Hängende Spitze'), ('Centre Forward', 'Stürmer'), ('Left Wing', 'Linker Flügel')], max_length=255),
        ),
    ]
