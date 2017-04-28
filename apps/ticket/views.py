from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.models import User
from apps.ticket.forms import TicketForm,EstablecimientoForm, TemaForm
from apps.ticket.models import Ticket, Establecimiento, Tema, Estado


# Create your views here.

def index(request):
    return render(request, 'ticket/index.html')

def ticket_view(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            print(obj.usuario)
            form.save()
        return redirect('ticket:ticket_list')
    else:
        form = TicketForm()
    return render(request, 'ticket/ticket_form.html', {'form': form})

def ticket_list(request):
    ticket = Ticket.objects.all().order_by('id')
    contexto = {'tickets': ticket}
    return render(request, 'ticket/ticket_list.html', contexto)

def ticket_edit(request, id_ticket):
    ticket = Ticket.objects.get(id=id_ticket)
    if request.method == "GET":
        form = TicketForm(instance=ticket)
    else:
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
        return redirect('ticket:ticket_list')
    return render(request, 'ticket/ticket_form.html', {'form': form})

def ticket_delete(request, id_ticket):
    ticket = Ticket.objects.get(id=id_ticket)
    if request.method == 'POST':
        ticket_delete()
        return redirect('ticket:ticket_list')
    return render(request, 'ticket/ticket_delete.html', {'ticket': ticket})

class TicketList(ListView):
    model = Ticket
    tempalte_name = 'ticket/ticket_list.html'

class TicketCreate(CreateView):
    model = Ticket
    form_class = TicketForm
    tempalte_name = 'ticket/ticket_form.html'
    success_url = reverse_lazy('ticket:ticket_list')

class TicketUpdate(UpdateView):
    model = Ticket
    form_class = TicketForm
    tempalte_name = 'ticket/ticket_form.html'
    success_url = reverse_lazy('ticket:ticket_list')

class TicketDelete(DeleteView):
    model = Ticket
    success_url = reverse_lazy('ticket:ticket_list')

def TemaCreate(request, value):
    if value == 'tema':
        form = TemaForm(request.POST)
        data = {'value' : 'tema'}
    elif value == 'establecimiento':
        form = EstablecimientoForm(request.POST)
        data = {'value': 'establecimiento'}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('ticket:ticket_form')
    else:
        form = TemaForm()
    return render(request, 'ticket/nuevo_form.html', {'form': form, 'data': data})

def EstadosView(request):
    total = Ticket.objects.filter().count()
    abierto = Ticket.objects.filter(estado_id=0).count()
    cerrado = Ticket.objects.filter(estado_id=1).count()
    pendiente = Ticket.objects.filter(estado_id=2).count()
    data = {
        'total':total,
        'abierto': abierto,
        'cerrado': cerrado,
        'pendiente': pendiente,
        }
    return render(request,"ticket/ticket_reportes.html", data)

def ticket_detalle(request, id_ticket):
    data ={
        'detalle': Ticket.objects.get(id=id_ticket)

        }
    print (data)

    return render(request,"ticket/ticket_detalle.html", data)

def Cambiar_estado(request, id_ticket, id_estado):
    print(id_ticket+' - '+id_estado)
    ticket = Ticket.objects.get(id=id_ticket)
    estado = Estado.objects.get(id=id_estado)
    ticket.estado = estado
    print(estado)
    ticket.save()
    return redirect('ticket:ticket_list')