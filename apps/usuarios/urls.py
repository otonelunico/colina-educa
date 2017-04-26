from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.usuarios.views import Cuenta_edit,\
    RegistroUsuario, ListUsuario, ModificarUsuario, EliminarUsuario, TecnicoCreate

urlpatterns = [
 #   url(r'^$', index, name='ticket'),
    url(r'^$', login_required(ListUsuario.as_view()), name='usuario_list'),
    url(r'^registrar', login_required(RegistroUsuario.as_view()), name='registrar'),
    url(r'^listar$', login_required(ListUsuario.as_view()), name='usuario_list'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(ModificarUsuario.as_view()), name='modif_usuario'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(EliminarUsuario.as_view()), name='elim_usuario'),
    url(r'^cuenta$', login_required(Cuenta_edit), name='Cuenta_edit'),
    url(r'^nuevo/tecnico', login_required(TecnicoCreate.as_view()), name='tecnico_form'),
]
