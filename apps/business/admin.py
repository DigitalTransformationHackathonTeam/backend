from django.contrib import admin
from business.models import Business, BusinessTag


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('id', 'business_type', 'business_name', 'eng_name')


admin.site.register(Business, BusinessAdmin)
admin.site.register(BusinessTag)
