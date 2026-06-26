from django.contrib import admin
from .models import Table, Reservation

@admin.register(Table) # Декоратор он привязывает настройки подели в админке
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seats')
    search_fields = ('number',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'date', 'hour_start', 'hour_end')
    list_filter = ('date', 'table')
    search_fields = ('user__username',)


