from django.db import models

# Create your models here.

class PlayerProfile(models.Model):
    """
    This class is where all the informations related to a player are centralized

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

	user              = models.OneToOneField(User, related_name='profile', null=True)
	timestamp_created = models.DateTimeField(_('date of creation'), default=timezone.now)
	timestamp_updated = models.DateTimeField(_('date of update'), default=timezone.now)
	registration_ip   = models.CharField(max_length=15, default='')

    class Meta:
        verbose_name        = _('player profile')
        verbose_name_plural = _('players profiles')

    def __unicode__(self):
        return self.user.username

