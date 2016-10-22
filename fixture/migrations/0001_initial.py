# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-22 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competition', '0001_initial'),
        ('team', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_home_team', models.PositiveSmallIntegerField()),
                ('goals_away_team', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('status', models.CharField(choices=[(1, 'SCHEDULED'), (2, 'TIMED'), (3, 'POSTPONED'), (4, 'IN_PLAY'), (5, 'CANCELED'), (6, 'FINISHED')], max_length=255)),
                ('matchday', models.PositiveSmallIntegerField()),
                ('home_team_name', models.CharField(max_length=255)),
                ('away_team_name', models.CharField(max_length=255)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='team.Team')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.Competition')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='team.Team')),
            ],
        ),
        migrations.CreateModel(
            name='HalfTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_home_team', models.PositiveSmallIntegerField()),
                ('goals_away_team', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Odds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_win', models.FloatField()),
                ('draw', models.FloatField()),
                ('away_win', models.FloatField()),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fixture.Fixture')),
            ],
        ),
        migrations.CreateModel(
            name='PenaltyShootout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_home_team', models.PositiveSmallIntegerField()),
                ('goals_away_team', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_home_team', models.PositiveSmallIntegerField(null=True)),
                ('goals_away_team', models.PositiveSmallIntegerField(null=True)),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fixture.Fixture')),
            ],
        ),
        migrations.AddField(
            model_name='penaltyshootout',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fixture.Result'),
        ),
        migrations.AddField(
            model_name='halftime',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fixture.Result'),
        ),
        migrations.AddField(
            model_name='extratime',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fixture.Result'),
        ),
    ]
