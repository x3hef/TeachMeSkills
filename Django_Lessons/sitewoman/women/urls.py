from multiprocessing.reduction import register

from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, 'year4')


urlpatterns = [
    path('', views.index, name='home'), # 127.0.0.1:8000/women
    path('about/', views.about, name='about'),
    path('post/<int:post_id>', views.show_post, name='post'),
]
