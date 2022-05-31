from django.db import models

# Create your models here.
class Vuelos(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    fecha_ida = models.DateField()
    
    class Meta:
        verbose_name = 'Vuelo'
        verbose_name_plural = 'Vuelos'