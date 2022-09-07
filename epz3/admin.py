from django.contrib import admin
from . models import Contact_Page


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)

admin.site.register(Contact_Page, ContactAdmin)
