from django.db import models
from django.contrib.auth.models import User

from apps.usuarios.models import Tecnico
# Create your models here.

"""
python3 manage.py makemigrationsheroku
python3 manage.py migrate

"""

class Estado(models.Model):
	titulo = models.CharField(max_length=50)
	def __str__(self):
		return '{}'.format(self.titulo)


class Establecimiento(models.Model):
	titulo = models.CharField(max_length=50)
	def __str__(self):
		return '{}'.format(self.titulo)

class Tema(models.Model):
	titulo = models.CharField(max_length=60)
	def __str__(self):
		return '{}'.format(self.titulo)

class Ticket(models.Model):
	usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	tema = models.ForeignKey(Tema, null=False, blank=True, on_delete=models.CASCADE)
	establecimiento = models.ForeignKey(Establecimiento, null=True, blank=True, on_delete=models.CASCADE)
	nom_contacto = models.CharField(max_length=50)
	ape_contacto = models.CharField(max_length=50)
	correo_contacto = models.EmailField()
	fijo_contacto = models.IntegerField()
	celu_contacto = models.IntegerField( null=True)
	resum_problema = models.CharField(max_length=100)
	asignado = models.ForeignKey(Tecnico, null=False, blank=True, on_delete=models.CASCADE)
	detall_problema = models.TextField()
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)
	estado =  models.ForeignKey(Estado, null=False, blank=True, on_delete=models.CASCADE)
	def __str__(self):
		return '{}'.format(self.resum_problema)
