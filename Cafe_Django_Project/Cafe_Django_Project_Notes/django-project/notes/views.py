from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Case, IntegerField, Value, When
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import NoteForm
from .models import Note
from .utils import SESSION_HISTORY_KEY, add_note_to_history


class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'

    def get_object(self, queryset=None):
        note = super().get_object(queryset=queryset)
        add_note_to_history(self.request, note.id)
        return note


class LastViewedNotesView(ListView):
    template_name = 'notes/view_history.html'
    context_object_name = 'notes'

    def get_queryset(self):
        history = self.request.session.get(SESSION_HISTORY_KEY, [])
        if not history:
            return Note.objects.none()

        preserved_order = Case(
            *[When(id=note_id, then=Value(position)) for position, note_id in enumerate(history)],
            output_field=IntegerField(),
        )
        return Note.objects.filter(id__in=history).order_by(preserved_order)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:note-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
