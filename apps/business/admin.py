from django.contrib import admin
from business.models import Business


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('id', 'business_type', 'business_name')


admin.site.register(Business, BusinessAdmin)
