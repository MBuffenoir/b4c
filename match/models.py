# -*- encoding: utf-8 -*-
from django.db import models

from player.models import PlayerProfile
from django.utils import timezone

# Create your models here.

    # {
    #     "map": "Prion Terraces",
    #     "type": "SOLO",
    #     "decision": "WIN",
    #     "speed": "FASTER",
    #     "date": 1448379900
    # }

class Match(models.Model):
    """
    This class is where all the informations related to a match are set. 
    """

    match_REGION = (
        (u'EU', u'Europe'),
        (u'NA', u'North America'),     
    )

    TYPE = (
        (u'PvZ','Protoss versus Zerg'),
        (u'PvT','Protoss versus Terran'),
        (u'PvP','Protoss versus Protoss'),
        (u'ZvZ','Zerg versus Zerg'),
        (u'ZvT','Zerg versus Terran'),
        (u'ZvP','Zerg versus Protoss'),
        (u'TvZ','Terran versus Zerg'),
        (u'TvT','Terran versus Terran'),
        (u'TvP','Terran versus Protoss'),
        (u'RvZ','Random, versus Zerg'),
        (u'RvT','Random, versus Terran'),
        (u'RvP','Random, versus Protoss'),
        (u'RvR','Random versus Random'),
    )

    FORMAT = (
        ('BO1','Best of 1'),
        ('BO3','Best of 3'),
        ('BO5','Best of 5'),
        ('BO7','Best of 7'),
    )

    owner             = models.ForeignKey(PlayerProfile, related_name='player', null=True)
    challenger        = models.ForeignKey(PlayerProfile, related_name='challenger', null=True)
    winner            = models.ForeignKey(PlayerProfile, related_name='winner', null=True)
    timestamp_created = models.DateTimeField('Date of creation', default=timezone.now)
    timestamp_updated = models.DateTimeField('Date of update', default=timezone.now)
    name              = models.CharField('Name of the game', max_length=64, null=True, blank=True)
    region            = models.CharField(max_length=12, choices=match_REGION, default='EU')
    type              = models.CharField(max_length=12, choices=TYPE, default='RvR')
    match_format      = models.CharField(max_length=12, choices=FORMAT, default='BO3')
    pot               = models.PositiveIntegerField('Pot amount in mBTC', default=0)
    played            = models.BooleanField('has the match been played yet ?', default=False)

    class Meta:
        verbose_name        = 'match'
        verbose_name_plural = 'matches'

    def __str__(self):
        return self.name