from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    ruc = models.CharField(max_length=13, unique=True)
    direccion = models.CharField(max_length=255)
    nombre_contacto = models.CharField(max_length=100)
    telefonos = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.nombre_empresa
    
class Catalogue(models.Model):
    nombre= models.CharField(max_length=250)
    precio=models.CharField(max_length=50)
    descripccion=models.CharField(max_length=250)
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} proveedor: {self.proveedor}"


class Stock(models.Model):
    catalogo=models.ForeignKey(Catalogue,on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    estacion = models.CharField(max_length=100)
    almacen = models.CharField(max_length=100)
    transporte = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.catalogo}"
    

