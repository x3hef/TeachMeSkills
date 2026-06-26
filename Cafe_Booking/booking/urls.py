from django.conf import settings
from django.urls import path, re_path
from . import views
import re
from django.views.static import serve

urlpatterns = [
    path('tables/', views.table_list, name='table_list'),
    path('reservations/new/', views.create_reservation, name='create_reservation'),
    path('reservations/my/', views.my_reservations, name='my_reservations'),
    path('reservations/delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
    path('reservation/edit/<int:pk>/', views.edit_reservation, name='edit_reservation'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
