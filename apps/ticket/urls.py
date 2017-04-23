from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.ticket.views import index, ticket_view, ticket_detalle, \
    TicketList, TicketCreate, TicketUpdate, TicketDelete, EstablecimientoCreate, TemaCreate, ReporteView
from apps.ticket.models import Ticket 

urlpatterns = [
   # url(r'^$', login_required(TicketCreate.as_view()), name='ticket_form'),
    url(r'^nuevo$', login_required(ticket_view), name='ticket_form'),
    url(r'^listar/$', login_required(TicketList.as_view()), name='ticket_list'),
    url(r'^listar/abiertos$', login_required(TicketList.as_view(queryset=Ticket.objects.filter(estado_id =0))), name='ticket_list_abierto'),
    url(r'^listar/cerrados$', login_required(TicketList.as_view(queryset=Ticket.objects.filter(estado_id =1))), name='ticket_list_cerrado'),
    url(r'^listar/pendientes$', login_required(TicketList.as_view(queryset=Ticket.objects.filter(estado_id =2))), name='ticket_list_pendiente'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(TicketUpdate.as_view()), name='ticket_edit'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(TicketDelete.as_view()), name='ticket_delete'),
    url(r'^nuevo/establ$', login_required(EstablecimientoCreate.as_view()), name='establ_form'),
    url(r'^nuevo/tema$', login_required(TemaCreate.as_view()), name='tema_form'),
    url(r'^reporte$', login_required(ReporteView), name='ticket_reporte'),
    url(r'^detalle/(?P<id_ticket>\d+)/$', login_required(ticket_detalle), name='ticket_detalle'),
    #url(r'^nuevo$', ticket_view, name='ticket_form'),
]
