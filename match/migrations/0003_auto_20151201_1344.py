# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_remove_playerprofile_registration_ip'),
        ('match', '0002_auto_20151129_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='challenger',
            field=models.ForeignKey(related_name='challenger', to='player.PlayerProfile', null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='match_format',
            field=models.CharField(default=b'BO3', max_length=12, choices=[(b'BO1', b'Best of 1'), (b'BO3', b'Best of 3'), (b'BO5', b'Best of 5'), (b'BO7', b'Best of 7')]),
        ),
        migrations.AddField(
            model_name='match',
            name='played',
            field=models.BooleanField(default=False, verbose_name=b'has the match been played yet ?'),
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(related_name='winner', to='player.PlayerProfile', null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='region',
            field=models.CharField(default=b'EU', max_length=12, choices=[('EU', 'Europe'), ('NA', 'North America')]),
        ),
    ]
