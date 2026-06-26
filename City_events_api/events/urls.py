from django.urls import path

from .views import (
    EventListView,
    EventSubscribeView,
    MyEventsView,
    UserListCreateView,
)

urlpatterns = [
    path("users", UserListCreateView.as_view(), name="users"),
    path("events", EventListView.as_view(), name="events"),
    path("events/my", MyEventsView.as_view(), name="my-events"),
    path("event/<int:id>", EventSubscribeView.as_view(), name="event-subscribe"),
]