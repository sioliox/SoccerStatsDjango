# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0020_auto_20170122_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('Keeper', 'Torwart'), ('Torwart', 'Torwart'), ('Abwehr', 'Abwehr'), ('Left-Back', 'Linker Außenverteidiger'), ('Linker Verteidiger', 'Linker Verteidiger'), ('Centre Back', 'Innenverteidiger'), ('Innenverteidiger', 'Innenverteidiger'), ('Right-Back', 'Rechter Außenverteidiger'), ('Rechter Verteidiger', 'Rechter Verteidiger'), ('Midfield', 'Mittelfeld'), ('Mittelfeld', 'Mittelfeld'), ('Defensive Midfield', 'Defensives Mittelfeld'), ('Defensives Mittelfeld', 'Defensives Mittelfeld'), ('Left Midfield', 'Linkes Mittelfeld'), ('Central Midfield', 'Zentrales Mittelfeld'), ('Zentrales Mittelfeld', 'Zentrales Mittelfeld'), ('Right Midfield', 'Rechtes Mittelfeld'), ('Attacking Midfield', 'Offensives Mittelfeld'), ('Offensives Mittelfeld', 'Offensives Mittelfeld'), ('Linksau&szlig;en', 'Linksaußen'), ('Left Wing', 'Linker Flügel'), ('Secondary Striker', 'Hängende Spitze'), ('H&auml;ngende Spitze', 'Hängende Spitze'), ('Centre Forward', 'Stürmer'), ('Mittelst&uuml;rmer', 'Mittelstürmer'), ('Right Wing', 'Rechter Flügel'), ('Rechtsau&szlig;en', 'Rechtsaußen')], max_length=255),
        ),
    ]