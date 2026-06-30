from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from notes.models import Note
from notes.utils import add_note_to_history

from .serializers import NoteSerializer


class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.select_related('author').all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NoteDetailAPIView(generics.RetrieveAPIView):
    queryset = Note.objects.select_related('author').all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        add_note_to_history(request, self.get_object().id)
        return response
