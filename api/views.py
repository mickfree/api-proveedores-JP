from rest_framework import viewsets
from .serializer import ProveedorSerializer
from .models import Proveedor 
# Create your views here.

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset= Proveedor.objects.all()
    serializer_class = ProveedorSerializer


