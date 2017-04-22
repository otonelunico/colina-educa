from django.db import models

# Create your models here.


class Tecnico(models.Model):
	usuario = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	correo = models.EmailField()
	def __str__(self):
		return '{}'.format(self.nombre+" "+self.apellido) 