from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from apps.usuarios.forms import RegistroForm,TecnicoForm
# Create your views here.

class RegistroUsuario(CreateView):
	model=User
	template_name ="auth/user_form.html"
	form_class = RegistroForm
	success_url = reverse_lazy('usuario:usuario_list')

class ListUsuario(ListView):
    model = User

class ModificarUsuario(UpdateView):
    model = User
    form_class = RegistroForm
    tempalte_name = "auth/registrar.html"
    success_url = reverse_lazy('usuario:usuario_list')


class EliminarUsuario(DeleteView):
    model = User
    success_url = reverse_lazy('usuario:usuario_list')

class TecnicoCreate(CreateView):
    model=User
    form_class = TecnicoForm
    template_name ="auth/tecnico_form.html"
    success_url = reverse_lazy('ticket:ticket_form')

def Cuenta_edit(request):
    userid = request.user.id
    obj = User.objects.get(id=userid)
    print(obj)
    if request.method == "GET":
        form = RegistroForm(instance=obj)
    else:
        form = RegistroForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        return redirect('usuario:modif_usuario')
    return render(request, 'auth/user_form.html', {'form': form})

