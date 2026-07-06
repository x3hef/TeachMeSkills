from django.urls import path
from .views import tables_list, create_reservation, my_reservations, signup, delete_reservation, restaurant_layout, \
    logout_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", restaurant_layout, name="home"),
    path('tables/', tables_list, name='tables_list'),
    path("reservations/new/", create_reservation, name="create_reservation"),
    path('reservations/my/', my_reservations, name='my_reservations'),
    path('signup/', signup, name='signup'),
    path('reservations/delete/<int:reservation_id>/', delete_reservation, name='delete_reservation'),
    path('restaurant-layout/', restaurant_layout, name='restaurant_layout'),
    path('logout/', logout_view, name='logout'),
    path('login/',LoginView.as_view(template_name='login.html'), name='login'
    ),

]
