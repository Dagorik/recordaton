from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class RegisterForm(ModelForm):

	class Meta:
		model = User
		fields = ["first_name", "last_name", "username", "password", "email"]
		widgets = {
			"password": forms.PasswordInput(attrs={
				"type": "password"
			})
		}

class LoginForm(forms.Form):

	username = forms.CharField(max_length=100, widget=
			forms.TextInput(attrs={'placeholder': "Escribe tu usuario"})
		)
	password = forms.CharField(max_length=100, widget=
			forms.PasswordInput(attrs={'type': 'password'})
		)