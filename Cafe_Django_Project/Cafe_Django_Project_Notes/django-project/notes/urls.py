from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='note-list'),
    path('create/', views.NoteCreateView.as_view(), name='note-create'),
    path('history/', views.LastViewedNotesView.as_view(), name='view-history'),
    path('<int:pk>/', views.NoteDetailView.as_view(), name='note-detail'),
]
