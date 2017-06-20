from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#python3 manage.py makemigrations
#python3 manage.py migrate

class Desde(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	cargo = models.CharField(max_length=100)
	activo = models.BooleanField(default=True)
	firma = models.TextField()
	def __str__(self):
		return '{}'.format(self.nombre+" "+self.apellidos)

class Para(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	cargo = models.CharField(max_length=100)
	activo = models.BooleanField(default=True)
	def __str__(self):
		return '{}'.format(self.nombre+" "+self.apellidos)

class Tipo_docum(models.Model):
	titulo = models.CharField(max_length=50)
	def __str__(self):
		return '{}'.format(self.titulo)

class Documento(models.Model):
	tipo= models.ForeignKey(Tipo_docum, null=False, blank=True, on_delete=models.CASCADE)
	num = models.IntegerField(null=False)
	ant = models.CharField(max_length=50, null=True)
	mat = models.CharField(max_length=50, null=False)
	desde = models.ForeignKey(Desde, null=False, blank=True, on_delete=models.CASCADE)
	para = models.ForeignKey(Para, null=False, blank=True, on_delete=models.CASCADE)
	cuerpo = models.TextField(null=False)
	piepag = models.TextField(null=False)
	creacion = models.TextField()
	ano =  models.TextField()
	usuario =  models.TextField()
	activo = models.BooleanField(default=True)

class Alertmessage(models.Model):
	tipo = models.CharField(max_length=50, null=True)
	message = models.CharField(max_length=50, null=True)
	dueno = models.IntegerField(null=True)
	def __str__(self):
		return '{}'.format(self.message)