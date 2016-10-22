# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-22 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Away',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.PositiveIntegerField()),
                ('goals_against', models.PositiveIntegerField()),
                ('wins', models.PositiveIntegerField()),
                ('draws', models.PositiveIntegerField()),
                ('losses', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CupTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_caption', models.CharField(max_length=255)),
                ('matchday', models.IntegerField()),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cup_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.CupTable')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GroupStanding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveSmallIntegerField()),
                ('played_games', models.PositiveSmallIntegerField()),
                ('crest_uri', models.URLField(null=True)),
                ('points', models.PositiveSmallIntegerField()),
                ('goals', models.PositiveSmallIntegerField()),
                ('goals_against', models.PositiveSmallIntegerField()),
                ('goal_difference', models.PositiveSmallIntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.Group')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.PositiveIntegerField()),
                ('goals_against', models.PositiveIntegerField()),
                ('wins', models.PositiveIntegerField()),
                ('draws', models.PositiveIntegerField()),
                ('losses', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LeagueTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_caption', models.CharField(max_length=255)),
                ('matchday', models.IntegerField()),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='Standing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('played_games', models.PositiveIntegerField()),
                ('points', models.PositiveIntegerField()),
                ('goals', models.PositiveIntegerField()),
                ('goals_against', models.PositiveIntegerField()),
                ('goal_difference', models.IntegerField()),
                ('wins', models.PositiveIntegerField()),
                ('draws', models.PositiveIntegerField()),
                ('losses', models.PositiveIntegerField()),
                ('league_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.LeagueTable')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team')),
            ],
        ),
        migrations.AddField(
            model_name='home',
            name='standing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.Standing'),
        ),
        migrations.AddField(
            model_name='away',
            name='standing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.Standing'),
        ),
    ]
