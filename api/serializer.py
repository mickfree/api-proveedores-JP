from rest_framework import serializers
from .models import *


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
<<<<<<< HEAD
        fields=('__all__')

class CatalogueSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Catalogue
        fields=('__all__')
        
class StockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stock
        fields=('__all__')
        
class SolicitudCompraSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SolicitudCompra
        fields = ('__all__')
        
class SolicitudProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SolicitudProducto
        fields = ('__all__')
=======
        fields=('__all__')
>>>>>>> 4e8dbca1ea3a1fcb5201a3424a90bf5c3445a249
