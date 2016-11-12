from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import *

class NoteListView(ListView):
	model = Note
	context_object_name = "notes" #para que no se llame object_list

class NoteDetailView(DetailView):
	model = Note

class NoteDeleteView(DeleteView):
	model = Note
	success_url = "/notes/list"

class NoteUpdateView(UpdateView):
	model = Note
	fields = []
	success_url = "/notes/list"

class NoteCreateView():
	model = Note
	fields = []
	success_url = "/notes/list"