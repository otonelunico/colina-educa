from django.shortcuts import render
from apps.cambios.models import Cambio
from apps.cambios.forms import CambioForm

# Create your views here.
def CambiosView(request):
    data = {'model': Cambio.objects.all(),
            'form': CambioForm(),
            'ultimo':Cambio.objects.last()}
    if request.method == 'POST':
        form = CambioForm(request.POST)
        if form.is_valid():
            data['val']=True
            form.save()
    return render(request, 'cambios/index.html', data)