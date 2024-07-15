from django.db import models

# Create your models here.

class Proveedor(models.Model):
    ruc = models.CharField(max_length=13, unique=True)
    direccion = models.CharField(max_length=255)
    nombre_contacto = models.CharField(max_length=100)
    items = models.TextField()
    telefonos = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.nombre_contacto
                               