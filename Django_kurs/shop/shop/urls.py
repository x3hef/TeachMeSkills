from django.contrib import admin
from django.urls import path, include

# главные URL адреса!
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
]
