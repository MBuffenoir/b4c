# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerprofile',
            name='display_name',
            field=models.CharField(null=True, verbose_name='blizzard player name', max_length=32, blank=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='player_id',
            field=models.PositiveIntegerField(null=True, verbose_name='blizzard player id', blank=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='primary_race',
            field=models.CharField(choices=[('P', 'Protoss'), ('Z', 'Zerg'), ('T', 'Terran')], max_length=12, default='P'),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='profile_path',
            field=models.CharField(null=True, verbose_name='path of the player profile', max_length=64, blank=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='region',
            field=models.CharField(choices=[('EU', 'Europe'), ('US', 'Partially executed')], max_length=12, default='EU'),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='season_loss',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='season_win',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='total_loss',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='total_win',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
