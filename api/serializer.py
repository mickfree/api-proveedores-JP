from rest_framework import serializers
from .models import *


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields=('__all__')
        
class CatalogueSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Catalogue
        fields=('__all__')