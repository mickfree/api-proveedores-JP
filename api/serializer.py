from rest_framework import serializers
from .models import *


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields=('__all__')