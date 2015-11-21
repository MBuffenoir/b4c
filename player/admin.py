from django.contrib import admin

from player.models import PlayerProfile

# Register your models here.

class PlayerProfileAdmin(ModelAdmin)
    search_fields   = ('user__username')
    
admin.site.register(PlayerProfile, PlayerProfileAdmin)
