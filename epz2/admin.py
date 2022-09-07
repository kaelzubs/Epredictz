from django.contrib import admin
from . models import About_Page
from django.db import models


# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)

admin.site.register(About_Page, AboutAdmin)
