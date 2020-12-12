from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width = "60" style="border-radius:50px;" />'.format(object.photo.url))

                                                                                                       
    list_display = ('id','thumbnail','name','designation','created_date')
    list_display_links = ('id','name',)
    search_fields = ('designation',)
    list_filter = ('designation',)

admin.site.register(Team,TeamAdmin)

