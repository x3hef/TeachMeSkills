from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.utils import timezone
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event
from .serializers import EventSerializer, UserRegistrationSerializer, UserSerializer

User = get_user_model()


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserRegistrationSerializer
        return UserSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class EventListView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        cached_data = cache.get('future_events')
        if cached_data is not None:
            return Response(cached_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        cache.set('future_events', serializer.data, 300)
        return Response(serializer.data)

    def get_queryset(self):
        return Event.objects.filter(meeting_time__gt=timezone.now()).order_by('meeting_time')


class EventSubscribeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        try:
            event = Event.objects.get(id=id, meeting_time__gt=timezone.now())
        except Event.DoesNotExist:
            return Response(
                {'error': 'Event not found or already started'},
                status=status.HTTP_404_NOT_FOUND,
            )

        if event.users.filter(id=request.user.id).exists():
            return Response({'message': 'You are already subscribed to this event'})

        event.users.add(request.user)
        return Response({'message': 'You subscribed to the event'}, status=status.HTTP_201_CREATED)


class MyEventsView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(
            users=self.request.user,
            meeting_time__gt=timezone.now(),
        ).order_by('meeting_time')
