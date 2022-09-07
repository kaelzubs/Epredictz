from django.contrib import admin
from . models import cookie_Page


# Register your models here.

class CookieAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)

admin.site.register(cookie_Page, CookieAdmin)
