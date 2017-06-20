from django import forms
from apps.cambios.models import Cambio


class CambioForm(forms.ModelForm):

	class Meta:
		model = Cambio
		fields = [
			'detalle',
		]
		labels = {
			'detalle':'Detalle',
		}
		widgets = {
			'detalle': forms.TextInput(attrs={'class':'form-control'}),
		}

