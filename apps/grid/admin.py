from django.contrib import admin
from grid.models import Grid, Cell


class CellAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 
                    'population', 'dist_to_underground')


admin.site.register(Grid)
admin.site.register(Cell, CellAdmin)
