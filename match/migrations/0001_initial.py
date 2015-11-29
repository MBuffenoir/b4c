# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_remove_playerprofile_registration_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of creation')),
                ('timestamp_updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of update')),
                ('name', models.CharField(verbose_name='Name of the game', max_length=64, null=True, blank=True)),
                ('region', models.CharField(default='EU', max_length=12, choices=[('EU', 'Europe'), ('US', 'Partially executed')])),
                ('race', models.CharField(default='RvR', max_length=12, choices=[('PvZ', 'Protoss versus Zerg'), ('PvT', 'Protoss versus Terran'), ('PvP', 'Protoss versus Protoss'), ('ZvZ', 'Zerg versus Zerg'), ('ZvT', 'Zerg versus Terran'), ('ZvP', 'Zerg versus Protoss'), ('TvZ', 'Terran versus Zerg'), ('TvT', 'Terran versus Terran'), ('TvP', 'Terran versus Protoss'), ('RvZ', 'Random, versus Zerg'), ('RvT', 'Random, versus Terran'), ('RvP', 'Random, versus Protoss'), ('RvR', 'Random versus Random')])),
                ('pot', models.PositiveIntegerField(default=0, verbose_name='Pot amount in mBTC')),
                ('owner', models.ForeignKey(to='player.PlayerProfile', related_name='player', null=True)),
            ],
            options={
                'verbose_name': 'match',
                'verbose_name_plural': 'matches',
            },
        ),
    ]
