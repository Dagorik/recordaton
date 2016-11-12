
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, DeleteView, CreateView, UpdateView
from .functions import authenticated
from .models import *

##Como pedir usuario autenticado en generic views?
class NoteListView(ListView):
	model = Note
	context_object_name = "notes" #para que no se llame object_list

	def get_queryset(self):
		queryset = Note.objects.filter(user = request.user.id)

class NoteDetailView(DetailView):
	model = Note

class NoteDeleteView(DeleteView):
	model = Note
	success_url = "/notes/list"

class NoteUpdateView(UpdateView):
	model = Note
	fields = ['note', 'priority', 'due_date', 'father_note']
	success_url = "/notes/list"

class NoteCreateView(CreateView):
	model = Note
	fields = ['note', 'priority', 'due_date', 'father_note', 'completed', 'image']
	success_url = "/notes/list"

class Login(View):

	form = LoginForm()

	def get(self, request, *args, **kwargs):
		
		return render(request,'index.html', {'form': self.form})

	def post(self, request, *args, **kwargs):
		self.form = LoginForm(request.POST)

		if self.form.is_valid():

			is_auth = authenticated(request, form.cleaned_data["username"], form.cleaned_data["password"])

			log = 'list-notes' if is_auth else 'index'
			return redirect(log)

class Register(View):

	form = RegisterForm()

	def get(self, request, *args, **kwargs):
		
		return render(request,'register.html', {'form': self.form})

	def post(self, request, *args, **kwargs):
		self.form = RegisterForm(request.POST)

		if self.form.is_valid():

			User.objects.create_user(
				first_name = self.form.cleaned_data["first_name"],
				last_name = self.form.cleaned_data["last_name"],
				username = self.form.cleaned_data["username"],
				password = self.form.cleaned_data["password"],
				email = self.form.cleaned_data["email"]
			)
			return redirect('list-notes')
