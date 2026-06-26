from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'meeting_time', 'place')
    search_fields = ('name', 'description', 'place')
    filter_horizontal = ('users',)
