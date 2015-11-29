from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

class PlayerProfile(models.Model):
    """
    This class is where all the informations related to a player are set. 

    informations available from blizzard player profile (from their API):
    
    'displayName': u'LaLu', u'clanName': u'', u'campaign': {u'wol': u'CASUAL', u'hots': u'HARD'}, u'career':
    '{u'protossWins': 2, u'seasonTotalGames': 6, u'primaryRace': u'PROTOSS', u'terranWins': 0, u'careerTotalGames':
    '2994, u'highestTeamRank': u'MASTER', u'highest1v1Rank': u'DIAMOND', u'zergWins': 0}, u'season': {u'seasonId': 24,
    'u'totalGamesThisSeason': 6, u'seasonNumber': 4, u'seasonYear': 2015}, u'realm': 1, u'portrait': {u'url':
    'u'http://media.blizzard.com/sc2/portraits/2-90.jpg', u'h': 90, u'w': 90, u'offset': 9, u'y': -90, u'x': -270},
    'u'profilePath': u'/profile/241726/1/LaLu/', u'swarmLevels': {u'zerg': {u'currentLevelXP': 0, u'totalLevelXP':
    '215000, u'level': 30}, u'protoss': {u'currentLevelXP': 95635, u'totalLevelXP': 225000, u'level': 34}, u'terran':
    '{u'currentLevelXP': 15581, u'totalLevelXP': 65000, u'level': 2}, u'level': 66}, u'clanTag': u'', u'id': 241726}
    """
    
    # user_id
    # display_name
    # region
    # total_level (sum of 3 races levels)
    # clan_name
    # primary_race
    # highest_1v1_rank
    # portrait
    # profile_path
    # rank
    # total_win
    # total_loss
    # season_win
    # season_loss

    player_REGION = (
        (u'EU', u'Europe'),
        (u'US', u'Partially executed'),     
    )

    RACE = (
        (u'P','Protoss'),
        (u'Z','Zerg'),
        (u'T','Terran'),
    )

    user              = models.OneToOneField(User, related_name='profile', null=True)
    timestamp_created = models.DateTimeField('date of creation', default=timezone.now)
    timestamp_updated = models.DateTimeField('date of update', default=timezone.now)
    player_id         = models.PositiveIntegerField('blizzard player id', null=True, blank=True)
    display_name      = models.CharField('blizzard player name', max_length=32, null=True, blank=True)
    region            = models.CharField(max_length=12, choices=player_REGION, default='EU')
    primary_race      = models.CharField(max_length=12, choices=RACE, default='P')
    profile_path      = models.CharField('path of the player profile', max_length=64, null=True, blank=True)
    total_win         = models.PositiveIntegerField(null=True, blank=True)
    total_loss        = models.PositiveIntegerField(null=True, blank=True)
    season_win        = models.PositiveIntegerField(null=True, blank=True)
    season_loss       = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name        = 'player profile'
        verbose_name_plural = 'players profiles'

    def __str__(self):
        return self.user.username

