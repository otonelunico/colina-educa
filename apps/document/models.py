from django.db import models

# Create your models here.
#python3 manage.py makemigrations
#python3 manage.py migrate

class Desde(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	cargo = models.CharField(max_length=100)
	def __str__(self):
		return '{}'.format(self.nombre+" "+self.apellidos+" - "+self.cargo) 

class Para(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	cargo = models.CharField(max_length=100)
	def __str__(self):
		return '{}'.format(self.nombre+" "+self.apellidos+" - "+self.cargo) 

class Tipo_docum(models.Model):
	titulo = models.CharField(max_length=50)
	def __str__(self):
		return '{}'.format(self.titulo)

class Documento(models.Model):
	tipo= models.ForeignKey(Tipo_docum, null=False, blank=True, on_delete=models.CASCADE)
	num = models.IntegerField(null=False)
	mat = models.CharField(max_length=50)
	desde = models.ForeignKey(Desde, null=False, blank=True, on_delete=models.CASCADE)
	para = models.ForeignKey(Para, null=False, blank=True, on_delete=models.CASCADE)
	cuerpo = models.TextField()
	creacion = models.DateTimeField(auto_now_add=True)
	modificacion = models.DateTimeField(auto_now=True)
	def __str__(self):
		return '{}'.format(self.num)

