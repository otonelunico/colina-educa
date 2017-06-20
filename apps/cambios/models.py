from django.db import models

# Create your models here.

class Cambio(models.Model):
    detalle = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{}'.format(self.detalle)
