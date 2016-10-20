# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-20 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=255)),
                ('league', models.CharField(choices=[(('440', 'CL'), ('432', 'DFB')), (('430', 'BL1'), ('431', 'BL2'))], max_length=255)),
                ('year', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)])),
                ('current_matchday', models.PositiveSmallIntegerField()),
                ('number_of_matchdays', models.PositiveSmallIntegerField()),
                ('number_of_teams', models.PositiveSmallIntegerField()),
                ('number_of_games', models.PositiveSmallIntegerField()),
                ('last_updated', models.DateTimeField()),
            ],
            options={
                'ordering': ['caption'],
            },
        ),
    ]
