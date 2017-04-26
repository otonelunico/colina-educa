from django import forms
from apps.document.models import Documento, Desde, Para

class DocumentoForm(forms.ModelForm):

	class Meta:
		model=Documento
		fields=[
			'tipo',
			'mat',
			'desde',
			'para',
			'cuerpo',
			'piepag',
		]
		labels={
			'tipo':'Tipo',
			'mat':'Mat',
			'desde':'Desde',
			'para':'Para',
			'cuerpo':'Cuerpo',
			'piepag':'Piepag',
		}
		widgets={
			'tipo':forms.Select(attrs={'class':'form-control'}),
			'mat': forms.TextInput(attrs={'class':'form-control'}),
			'desde': forms.Select(attrs={'class':'form-control'}),
			'para': forms.Select(attrs={'class':'form-control'}),
			'cuerpo': forms.Textarea(attrs={'class':'form-control'}),
			'piepag': forms.Textarea(attrs={'class':'form-control'}),
			}
			
class DesdeForm(forms.ModelForm):

	class Meta:
		model = Desde
		fields = [
			'nombre',
			'apellidos',
			'cargo',
		]
		labels = {
			'nombre':'Nombre',
			'apellidos':'Apellidos',
			'cargo':'Cargo',

		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'cargo': forms.TextInput(attrs={'class':'form-control'}),

		}


class ParaForm(forms.ModelForm):

	class Meta:
		model = Para
		fields = [
			'nombre',
			'apellidos',
			'cargo',
		]
		labels = {
			'nombre':'Nombre',
			'apellidos':'Apellidos',
			'cargo':'Cargo',

		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'cargo': forms.TextInput(attrs={'class':'form-control'}),

		}

