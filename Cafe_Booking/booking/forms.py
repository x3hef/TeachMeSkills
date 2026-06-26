from django import forms
from .models import Reservation, Table
from django.utils import timezone # Для работы с временем

class ReservationForm(forms.ModelForm):
    """ФОРМА БРОНИРОВАНИЯ"""
    class Meta:
        model = Reservation
        fields = ('table', 'date', 'hour_start', 'hour_end')

    def clean(self):
        """Валидация"""
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        table = cleaned_data.get('table')
        hour_start = cleaned_data.get('hour_start')
        hour_end = cleaned_data.get('hour_end')

        if date and date < timezone.now().date():
            raise forms.ValidationError("Нельзя забронировать на прошедшую дату!")

        if hour_start < 8 or hour_end > 18:
            raise forms.ValidationError("Мы работаем только с 8:00 до 18:00")

        if hour_start and hour_end and hour_end <= hour_start:
            raise forms.ValidationError("Время завершения не должно быть позже времени начала!")

        # Проверка занятости стола
        overlap = Reservation.objects.filter(
            table=table,
            date=date,
            hour_start__lt=hour_start, # это __lt меньше чем
            hour_end__gt=hour_end # это __gt больше чем
        ).exists()

        if overlap:
            raise forms.ValidationError(f"Столик №{table.number} уже занят в этот промежуток времени! ❌")

        return cleaned_data
