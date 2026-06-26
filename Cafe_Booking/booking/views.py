from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation
from .models import Table
from django.shortcuts import get_object_or_404


@login_required  # Только для тех кто зашел на сайт
def create_reservation(request):
    """Создание модели брони"""
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('my_reservations')
    else:
        form = ReservationForm()

    return render(request, 'booking/reservation_form.html', {'form': form})


@login_required
def my_reservations(request):
    """Список броней"""
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'booking/my_reservations.html', {'reservations': reservations})


def table_list(request):
    tables = Table.objects.all()
    return render(request, 'booking/table_list.html', {'tables': tables})


@login_required
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, "Бронирование успешно отменено. Ждем вас в другой раз! 😊")
        return redirect('my_reservations')

    return render(request, 'booking/confirm_delete.html', {'reservation': reservation})


@login_required
def book_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, f'Ура! Столик №{reservation.table.number} успешно забронирован!')
            return redirect('my_reservations')
    else:
        form = ReservationForm()

    return render(request, 'booking/book_table.html', {'form': form})


@login_required
def edit_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Бронирование успешно обновлено! ✨")
            return redirect('my_reservations')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'booking/edit_reservation.html', {'form': form, 'reservation': reservation})


def home_view(request):
    tables = Table.objects.all()
    return render(request, 'booking/table_list.html', {'tables': tables})