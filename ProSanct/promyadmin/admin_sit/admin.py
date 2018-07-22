from django.contrib import admin
from admin_sit.models import *

# Register your models here.
class DataAdmin(admin.ModelAdmin):
	list_display=['brandname','textread','thumbnail_tag','bannertype']
	list_filter=['brandname','category','bannertype']
	search_fields=['brandname']
	#fields = ['image_tag','website','textread','category','percentageoff']
	fieldsets = [
	    ('Brand Information', {'fields': ['brandname']}),
        ('Image',               {'fields': ['image_tag']}),
        ('Sales Information', {'fields': ['city','category','salestype','percentageoff','bannertype','startdate','enddate','extractiondate']}),
        ('Dummy Information',{'fields':['city']})

    ]

	readonly_fields = ['image_tag','brandname']
class WarningAdmin(admin.ModelAdmin):
	list_display=['sentby','warning']
	list_filter=['sentby']
class BrandAdmin(admin.ModelAdmin):
	list_display=['brandname','tag','attribute','value']
admin.site.register(DarazData,DataAdmin)
admin.site.register(Brands,BrandAdmin)
admin.site.register(Warnings,WarningAdmin)
