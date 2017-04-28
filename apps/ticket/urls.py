from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.ticket.views import index, ticket_view, ticket_detalle, Cambiar_estado, \
    TicketList, TicketCreate, TicketUpdate, TicketDelete, TemaCreate, EstadosView
from apps.ticket.models import Ticket 

urlpatterns = [
    url(r'^$', login_required(EstadosView), name='ticket_home'),
    url(r'^nuevo$', login_required(ticket_view), name='ticket_form'),
    url(r'^listar/$', login_required(TicketList.as_view()), name='ticket_list'),
    url(r'^listar/abiertos$', login_required(TicketList.as_view(queryset=Ticket.objects.filter(estado_id =0))), name='ticket_list_abierto'),
    url(r'^listar/cerrados$', login_required(TicketList.as_view(queryset=Ticket.objects.filter(estado_id =1))), name='ticket_list_cerrado'),
    url(r'^listar/pendientes$', login_required(TicketList.as_view(queryset=Ticket.objects.filter(estado_id =2))), name='ticket_list_pendiente'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(TicketUpdate.as_view()), name='ticket_edit'),
    url(r'^estado/(?P<id_ticket>\d+)/(?P<id_estado>\d+)/$', login_required(Cambiar_estado), name='estado_edit'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(TicketDelete.as_view()), name='ticket_delete'),
   url(r'^nuevo/(?P<value>\w+)', login_required(TemaCreate), name='nuevo_form'),
    url(r'^estados$', login_required(EstadosView), name='ticket_estados'),
    url(r'^detalle/(?P<id_ticket>\d+)/$', login_required(ticket_detalle), name='ticket_detalle'),
    #url(r'^nuevo$', ticket_view, name='ticket_form'),
]
