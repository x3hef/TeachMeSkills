from django import forms
from datetime import date, time

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Reservation


class ReservationForm(forms.ModelForm):

    class Meta:

        model = Reservation

        fields = [
            'table',
            'date',
            'hour_start',
            'hour_end',
        ]

        widgets = {

            'date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'hour_start': forms.TimeInput(
                attrs={
                    'type': 'time'
                }
            ),

            'hour_end': forms.TimeInput(
                attrs={
                    'type': 'time'
                }
            ),

        }

    def clean_date(self):

        reservation_date = self.cleaned_data['date']

        if reservation_date < date.today():

            raise forms.ValidationError(
                "Нельзя бронировать на прошлую дату"
            )

        return reservation_date

    def clean(self):

        cleaned_data = super().clean()

        table = cleaned_data.get('table')
        date_value = cleaned_data.get('date')
        hour_start = cleaned_data.get('hour_start')
        hour_end = cleaned_data.get('hour_end')


        if hour_start and hour_end:

            if hour_start >= hour_end:

                raise forms.ValidationError(
                    "Время окончания должно быть позже начала"
                )

            if hour_start < time(8, 0):

                raise forms.ValidationError(
                    "Кафе работает с 08:00"
                )

            if hour_end > time(18, 0):

                raise forms.ValidationError(
                    "Кафе работает до 18:00"
                )

        if table and date_value and hour_start and hour_end:

            exists = Reservation.objects.filter(
                table=table,
                date=date_value,
                hour_start__lt=hour_end,
                hour_end__gt=hour_start,
            ).exists()

            if exists:

                raise forms.ValidationError(
                    "Этот столик уже занят на выбранное время"
                )

        return cleaned_data


class SignUpForm(UserCreationForm):

    class Meta:

        model = User

        fields = [
            'username',
            'password1',
            'password2',
        ]