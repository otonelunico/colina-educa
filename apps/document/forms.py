from django import forms
from apps.document.models import Documento, Desde, Para

class DocumentoForm(forms.ModelForm):

	class Meta:
		model=Documento
		fields=[
			'tipo',
			'num',
			'mat',
			'desde',
			'para',
			'cuerpo',
		]
		labels={
			'tipo':'Tipo',
			'num':'Num',
			'mat':'Mat',
			'desde':'Desde',
			'para':'Para',
			'cuerpo':'Cuerpo',
		}
		widgets={
			'tipo':forms.Select(attrs={'class':'form-control'}),
			'num': forms.TextInput(attrs={'class':'form-control'}),
			'mat': forms.TextInput(attrs={'class':'form-control'}),
			'desde': forms.Select(attrs={'class':'form-control'}),
			'para': forms.Select(attrs={'class':'form-control'}),
			'cuerpo': forms.Textarea(attrs={'class':'form-control'}),
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

