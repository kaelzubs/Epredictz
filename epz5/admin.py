from django.contrib import admin
from . models import faq_Page

# Register your models here.

class DisclaimAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)

admin.site.register(faq_Page, DisclaimAdmin)
