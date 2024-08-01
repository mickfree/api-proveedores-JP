from rest_framework import viewsets
<<<<<<< HEAD
from .serializer import *
from .models import *
=======
from .serializer import ProveedorSerializer
from .models import Proveedor 
>>>>>>> 4e8dbca1ea3a1fcb5201a3424a90bf5c3445a249
# Create your views here.

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset= Proveedor.objects.all()
    serializer_class = ProveedorSerializer


<<<<<<< HEAD
class CatalogueViewSet(viewsets.ModelViewSet):
    queryset=Catalogue.objects.all()
    serializer_class = CatalogueSerializer
    
    
class StockViewSet(viewsets.ModelViewSet):
    queryset=Stock.objects.all()
    serializer_class= StockSerializer
    
class SolicitudCompraViewSet(viewsets.ModelViewSet):
    queryset=SolicitudCompra.objects.all()
    serializer_class = SolicitudCompraSerializer
    
class SolicitudProductoViewSet(viewsets.ModelViewSet):
    queryset = SolicitudProducto.objects.all()
    serializer_class = SolicitudProductoSerializer
    
=======
>>>>>>> 4e8dbca1ea3a1fcb5201a3424a90bf5c3445a249
