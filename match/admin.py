from django.contrib import admin

from match.models import Match

# Register your models here.

class MatchAdmin(admin.ModelAdmin):
    search_fields   = ('owner__name',)
    
admin.site.register(Match, MatchAdmin)
