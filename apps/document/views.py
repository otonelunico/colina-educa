from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.document.models import Documento, Para, Desde
from apps.document.forms import DocumentoForm, DesdeForm, ParaForm
import datetime, time
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors


# Create your views here.

class DocumentoCreate(CreateView):
    model = Documento
    form_class = DocumentoForm
    tempalte_name = 'ticket/ticket_form.html'
    success_url = reverse_lazy('document:document_form')

def Fecha_actual():
    x = datetime.datetime.now()
    y = time.strftime("%A")

    def sw_dia(x):
        return {
            'Monday': 'Lunes',
            'Tuesday': 'Martes',
            'Wednesday': 'Miercoles',
            'Thursday': 'Jueves',
            'Friday': 'Viernes',
            'Saturday': 'Sabado',
            'Sunday': 'Domingo',
        }[x]

    def sw_mes(x):
        return {
            1: 'Enero',
            2: 'Febrero',
            3: 'Marzo',
            4: 'Abril',
            5: 'Mayo',
            6: 'Junio',
            7: 'Julio',
            8: 'Agosto',
            9: 'Septiembre',
            10: 'Octubre',
            11: 'Noviembre',
            12: 'Diciembre',
        }[x]

    fecha = {
        'ndia': sw_dia(y),
        'dia': x.day,
        'mes': sw_mes(x.month),
        'año': x.year
    }
    return fecha

def Document_create(request):
    try:
        doc_ant = Documento.objects.latest('id')
        val=True
    except Documento.DoesNotExist:
        doc_ant = {
            'num':0,
            'piepag':'',
        }
        val=False

    fecha = Fecha_actual()
    fecha_str = str(fecha['dia'])+" "+fecha['mes']+" "+str(fecha['año'])
    print (doc_ant.año+' '+str(fecha['año']))
    if request.method == 'POST':
        form = DocumentoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            if val and doc_ant.año==str(fecha['año']):
                obj.num = doc_ant.num+1
            else:
                obj.num = 1
            obj.creacion = fecha_str
            obj.año = fecha['año']

            form.save()
        else:
            print(form.is_valid())
            print(form.errors)
            form = DocumentoForm(request.POST)
        return redirect('document:documento_list')
    else:
        form = DocumentoForm()
    print (doc_ant)
    if val:
        data={
            'pie_anterior': doc_ant.piepag,
            'num': doc_ant.num #cambiar por el siguiente numeromde la base de datos
            }
    else:
        data = {
            'pie_anterior': 'Texto',
            'num': doc_ant['num']  # cambiar por el siguiente numeromde la base de datos
        }
    return render(request, 'document/documento_form.html', dict(form=form, fecha=fecha, data=data))


class ParaCreate(CreateView):
    model = Para
    form_class = ParaForm
    template_name ="document/nuevo_desdepara.html"
    success_url = reverse_lazy('document:document_form') 

class DesdeCreate(CreateView):
    model = Desde
    form_class = DesdeForm
    template_name ="document/nuevo_desdepara.html"
    success_url = reverse_lazy('document:document_form')

class Document_list(ListView):
    model = Documento
    tempalte_name = 'document/documento_list.html'

def Pdf_documento():

    tempalte_name = 'document/documento_list.html'