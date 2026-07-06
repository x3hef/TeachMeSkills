from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import ReservationForm, SignUpForm
from .models import Table, Reservation
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


def tables_list(request):
    seats = request.GET.get("seats")

    if seats:

        tables = Table.objects.filter(
            seats=seats
        )

    else:

        tables = Table.objects.all()

    context = {
        "tables": tables,
        "selected_seats": seats,
    }

    return render(
        request,
        "tables_list.html",
        context
    )


def create_reservation(request):

    if not request.user.is_authenticated:
        return redirect("login")

    table_id = request.GET.get("table")

    table = None

    if table_id:
        table = get_object_or_404(
            Table,
            id=table_id
        )

    if request.method == "POST":

        form = ReservationForm(
            request.POST
        )

        if form.is_valid():

            reservation = form.save(
                commit=False
            )

            reservation.user = request.user

            if table:
                reservation.table = table

            reservation.save()

            return redirect(
                "my_reservations"
            )

    else:

        if table:

            form = ReservationForm(
                initial={
                    "table": table
                }
            )

            form.fields["table"].widget.attrs[
                "style"
            ] = "display:none"

        else:

            form = ReservationForm()

    context = {
        "form": form,
        "table": table
    }

    return render(
        request,
        "reservation_form.html",
        context
    )


@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user).order_by("-date")
    context = {
        "reservations": reservations
    }

    return render(request, "my_reservations.html", context)


def signup(request):
    if request.method == "POST":

        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")
    else:
        form = SignUpForm()

    return render(request, "signup.html", {"form": form})


@login_required  # Декоратор проверки вошел не вошел пользователь.
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(  # найти бронь если нет то 404. Такая логика
        Reservation,
        id=reservation_id,
        user=request.user
    )

    reservation.delete()

    return redirect("my_reservations")


def restaurant_layout(request):
    tables = Table.objects.all()

    context = {
        "tables": tables
    }

    return render(
        request,
        "restaurant_layout.html",
        context
    )

def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(
        user=request.user
    )

    return render(
        request,
        'my_reservations.html',
        {
            'reservations': reservations
        }
    )