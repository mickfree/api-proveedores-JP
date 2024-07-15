from rest_framework import viewsets
from .serializer import *
from .models import *
# Create your views here.

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset= Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class CatalogueViewSet(viewsets.ModelViewSet):
    queryset=Catalogue.objects.all()
    serializer_class = CatalogueSerializer