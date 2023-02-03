from django.contrib import admin
from . models import Home_Page

# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'league', 'home_team', 'away_team', 'tip', 'tip_odd', 'result')
    search_fields = ('date_time', 'league')
    prepopulated_fields = {'slug': ('league',), }
admin.site.register(Home_Page, HomeAdmin)
