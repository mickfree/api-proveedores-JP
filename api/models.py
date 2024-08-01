from django.db import models
from decimal import Decimal
import uuid

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
    nombre = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=250)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} proveedor: {self.proveedor}"

class Stock(models.Model):
    catalogo = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    estacion = models.CharField(max_length=100)
    almacen = models.CharField(max_length=100)
    transporte = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.catalogo}"

class SolicitudCompra(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    fecha = models.DateField(auto_now_add=True)
    productos = models.ManyToManyField(Catalogue, through='SolicitudProducto', blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    entrega = models.DateField()
    pago = models.DateField()
    estado = models.CharField(max_length=50)
    
    def save(self, *args, **kwargs):
        if not self.numero:
            self.numero = str(uuid.uuid4())
        super(SolicitudCompra, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.numero} proveedor: {self.proveedor}"

    
class SolicitudProducto(models.Model):
    solicitud = models.ForeignKey(SolicitudCompra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.solicitud} - {self.producto.nombre}'

