from django.contrib.auth.models import User
from django.utils import timezone

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Event
from .serializers import EventSerializer, UserRegistrationSerializer, UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserRegistrationSerializer
        return UserSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class EventListView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Event.objects.filter(meeting_time__gt=timezone.now())


class EventSubscribeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        try:
            event = Event.objects.get(id=id, meeting_time__gt=timezone.now())
        except Event.DoesNotExist:
            return Response(
                {"error": "Event not found or already started"},
                status=404,
            )

        event.users.add(request.user)

        return Response({"message": "You subscribed to the event"})


class MyEventsView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(
            users=self.request.user,
            meeting_time__gt=timezone.now(),
        )
