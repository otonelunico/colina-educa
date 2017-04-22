from django.shortcuts import render, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.document.models import Documento, Para, Desde
from apps.document.forms import DocumentoForm, DesdeForm, ParaForm

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

class Documentopdf(View):  
 
    def cuerpo(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/imagenes/logo.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 700, 220, 90,preserveAspectRatio=True)    
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 14)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(350, 760, u"NUM.: 2017001")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(350, 730, u"MAT.: COMUNICADO") 
        pdf.setFont("Helvetica", 12)
        pdf.drawString(80, 670, u"COLINA, VIERNES, 27 DE ENERO 2017") 
        pdf.setFont("Helvetica", 12)
        pdf.drawString(280, 620, u"OFICIO")     
        pdf.setFont("Helvetica", 12)
        pdf.drawString(80, 570, u"DE:")   
        pdf.setFont("Helvetica", 12)
        pdf.drawString(80, 530, u"PARA:")   
        pdf.setFont("Helvetica", 12)
        pdf.drawString(240, 480, u"Junto con saludarle, comunico a usted que al funcionario Mario Silva Hernández, RUT:17.577.989-2, NO se le renovará el contrato de trabajo para el nuevo periodo. El contrato actual tiene vigencia hasta el 28 de febrero 2017. Sin otro particular le Saluda atentamente.")
    
    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('ID', 'Nombre', 'Apellido ', 'Cargo')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = [('ADSAS','''<b>precio_unitarifvfsdvghdefdwfewo</b>''', 'ASASAS', 'ASAS') ]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 5 * cm, 5 * cm, 5 * cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60,y)

    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cuerpo(pdf)
        y = 400
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response