from django.contrib import admin
from . models import Home_Page

# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ('match_dat', 'match_time', 'country', 'league', 'home_team', 'away_team', 'tip', 'tip_odd', 'result')
    search_fields = ('match_dat',)

admin.site.register(Home_Page, HomeAdmin)
