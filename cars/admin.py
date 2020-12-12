from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width = "60" style="border-radius:50px;" />'.format(object.car_photo.url))

                                                                                                       
    list_display = ('id','thumbnail','car_title','city','model','color','year','body_style','fuel_type','is_featured')
    list_display_links = ('id','car_title',)
    search_fields = ('name','model','car_title',)
    

admin.site.register(Car,CarAdmin)