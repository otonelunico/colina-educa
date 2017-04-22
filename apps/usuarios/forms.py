
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.usuarios.models import Tecnico

class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username':'Nombre de usuario',
				'first_name':'Nombre',
				'last_name':'Apellido',
				'email':'Correo',
		} 
		widgets = {
			'username': forms.TextInput(attrs={'class':'form-control'}),
			'first_name': forms.TextInput(attrs={'class':'form-control'}),
			'last_name': forms.TextInput(attrs={'class':'form-control'}),
			'establecimiento': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
		}

class TecnicoForm(forms.ModelForm):

	class Meta:
		model=Tecnico
		fields = [
			'usuario',
			'nombre',
			'apellido',
			'correo',
			]
		labels = {
			'usuario':'Usuario',
			'nombre':'Nombre',
			'apellido':'Apellido',
			'correo':'Correo',
		}
		widgets = {
			'usuario': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'correo': forms.TextInput(attrs={'class':'form-control'}),
		}