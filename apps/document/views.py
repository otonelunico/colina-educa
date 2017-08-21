from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.document.models import Documento, Para, Desde, Tipo_docum, Alertmessage
from apps.document.forms import DocumentoForm, DesdeForm, ParaForm
import datetime, time

# Create your views here.

class DocumentoCreate(CreateView):
    model = Documento
    data = {'value' :'documento'}
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
        'ano': x.year
    }
    return fecha

def Document_create(request):
    try:
        doc_ant = Documento.objects.latest('id')
        val = True
    except Documento.DoesNotExist:
        doc_ant = {
            'num': 0,
            'piepag': '',
        }
        val = False
    fecha = Fecha_actual()
    fecha_str = fecha['ndia']+", "+str(fecha['dia']) + " de " + fecha['mes'] + " del " + str(fecha['ano'])
    if val:
        data = {
            'pie_anterior': doc_ant.piepag,
            'num': doc_ant.num,  # cambiar por el siguiente numeromde la base de datos
        }
    else:
        data = {
            'pie_anterior': '',
            'num': doc_ant['num']  # cambiar por el siguiente numeromde la base de datos
        }
    if request.method == 'POST':
        form = DocumentoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            tipo_ant = Documento.objects.filter(tipo=obj.tipo)
            doc_ant=tipo_ant.last()
            if val and doc_ant.ano == str(fecha['ano']):
                obj.num = int(doc_ant.num) + 1
            else:
                obj.num = 1
            obj.creacion = fecha_str
            obj.ano = fecha['ano']
            valdos = 0
            if obj.desde != doc_ant.desde:
                valdos = valdos + 1
            if obj.para != doc_ant.para:
                valdos = valdos + 1
            if obj.cuerpo != doc_ant.cuerpo:
                valdos = valdos + 1
            if obj.mat != doc_ant.mat:
                valdos = valdos + 1


            if valdos < 2:
                Documento.objects.filter(id=doc_ant.id).update(num = doc_ant.num,
                                                               mat = obj.mat,
                                                               desde = obj.desde,
                                                               para = obj.para,
                                                               cuerpo = obj.cuerpo,
                                                               piepag = obj.piepag)


                obj.id = doc_ant.id

                setMessage('estandar', 'Se ha modificado el documento.', obj.id)
            else:
                form.save()
            return redirect('document:documento_detalle', obj.id)
        else:
            print(form.is_valid())
            print(form.errors)
            form = DocumentoForm(request.POST)

    else:
        form = DocumentoForm()



    data['ant'] = Documento.objects.all().order_by('-id')[:20]
    data['desde'] = Desde.objects.filter(activo=True).order_by('id')
    data['para'] = Para.objects.filter(activo=True).order_by('id')
    data['tipo'] = Tipo_docum.objects.all().order_by('id')

    return render(request, 'document/documento_form.html', dict(form=form, fecha=fecha, data=data))

def Create_value(request, value):
    if value == 'desde':
        data = {'titulo': 'Remitente',
                'tema': 'remitente',
                'value': value}
        model = Desde.objects.all().order_by('nombre')
        form= DesdeForm()
        if request.method == 'POST':
            form = DesdeForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('document:create_value', value)
    elif value == 'para':
        data={'titulo' :'Destinatario',
              'tema' : 'destinatario',
                'value': value}
        model = Para.objects.all().order_by('nombre')
        form= ParaForm()
        if request.method == 'POST':
            form = ParaForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('document:create_value', value)

    return render(request, 'document/create_value.html', {'form' :form, 'model': model, 'data': data})

def Edit_value(request, value, id_value):
    if value == 'desde':
        data = {'titulo': 'Remitente',
                'tema': 'remitente',
                'value': value}
        model = Desde.objects.all().order_by('nombre')
        modelform = Desde.objects.get(id = id_value)
        if request.method == 'GET':
            form = DesdeForm(instance=modelform)
        else:
            form = DesdeForm(request.POST, instance=modelform)
            if form.is_valid():
                form.save()
            return redirect('document:create_value', value)

    elif value == 'para':
        data={'titulo' :'Destinatario',
              'tema' : 'destinatario',
                'value': value}
        model = Para.objects.all().order_by('nombre')
        modelform = Para.objects.get(id=id_value)
        if request.method == 'GET':
            form = DesdeForm(instance=modelform)
        else:
            form = ParaForm(request.POST, instance=modelform)
            if form.is_valid():
                form.save()
            return redirect('document:create_value', value)

    return render(request, 'document/create_value.html', {'form' :form, 'model': model, 'data': data, 'modelform': modelform})

def Active_off(request, value, id_value):
    if value == 'desde':
        value_ = Desde.objects.get(id=id_value)
        value_.activo = False
        value_.save()
        return redirect('document:create_value', value)
    elif value == 'para':
        value_ = Para.objects.get(id=id_value)
        value_.activo = False
        value_.save()
        return redirect('document:create_value', value)
    elif value == 'documento':
        value_ = Documento.objects.get(id=id_value)
        value_.activo = False
        value_.save()
        return redirect('document:documento_list')

def Documento_edit(request, id_documento):
    model = Documento.objects.get(id=id_documento)
    data={'pie_anterior': model.piepag,
          'cuerpo': model.cuerpo}
    if request.method == "GET":
        form = DocumentoForm(instance=model)
    else:
        form = DocumentoForm(request.POST, instance=model)
        if form.is_valid():
            obj = form.save(commit=False)
            _obj=Documento.objects.get(num = obj.num, tipo = obj.tipo)
            form.save()

            setMessage('estandar', 'Se a modificado el documento.', _obj.id)
            return redirect('document:documento_detalle', _obj.id)
    fecha = Fecha_actual()
    data['ant'] = Documento.objects.all().order_by('-id')[:20]
    data['desde'] = Desde.objects.filter(activo=True).order_by('id')
    data['para'] = Para.objects.filter(activo=True).order_by('id')
    data['tipo'] = Tipo_docum.objects.all().order_by('id')
    return render(request, 'document/documento_form.html', {'form': form,'data': data, 'fecha': fecha})

def Documento_list(request):
    model = Documento.objects.all().order_by('-id')
    return render(request, 'document/documento_list.html', {'model': model})

def Detalle_doc(request, id_docum):
    model = Documento.objects.get(id=id_docum)
    msj = getMessage('estandar')
    mensaje = 'null'
    if msj.message !="null" and msj.dueno == model.id:
        mensaje = getMessage('estandar').message
        setMessage('estandar','null',model.id )

    data = {
        'detalle': model,
        'alert': mensaje
    }

    return render(request, "document/detalle_documento.html", data)

def getMessage(tipo):
      return Alertmessage.objects.get(tipo=tipo)

def setMessage(tipo, msj, id):
      obj = Alertmessage.objects.get(tipo=tipo)
      obj.message = msj
      obj.dueno = id
      obj.save()