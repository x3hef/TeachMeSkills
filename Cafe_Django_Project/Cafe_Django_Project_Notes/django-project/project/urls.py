from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import include, path, reverse_lazy
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from table import views as table_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', table_views.IndexView.as_view(), name='index'),
    path('tables/', include('table.urls')),
    path('reservation/', include('reservation.urls')),
    path('auth/', include('authentication.urls')),
    path('notes/', include('notes.urls')),

    path('api/reservations/', include('reservation.api.urls')),
    path('api/users/', include('authentication.api.urls')),
    path('api/notes/', include('notes.api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('auth/password-reset/', PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        success_url=reverse_lazy('password_reset_done'),
    ), name='password_reset'),
    path('auth/password-reset/done/', PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html',
    ), name='password_reset_done'),
    path('auth/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url=reverse_lazy('password_reset_complete'),
    ), name='password_reset_confirm'),
    path('auth/reset/done/', PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html',
    ), name='password_reset_complete'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += debug_toolbar_urls()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
