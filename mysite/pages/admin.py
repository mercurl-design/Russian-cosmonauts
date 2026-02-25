from django.contrib import admin
from .models import Cosmonaut

@admin.register(Cosmonaut)
class CosmonautAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'total_flights', 'total_space_time', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'achievements')
    list_filter = ('first_flight',)