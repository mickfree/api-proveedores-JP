from django.urls import path,include
<<<<<<< HEAD
from rest_framework import routers
=======
from  rest_framework import routers
>>>>>>> 4e8dbca1ea3a1fcb5201a3424a90bf5c3445a249
from api import views

router=routers.DefaultRouter()
router.register(r'proveedores',views.ProveedorViewSet)
<<<<<<< HEAD
router.register(r'catalogues', views.CatalogueViewSet)
router.register(r'stock',views.StockViewSet)
router.register(r'compra',views.SolicitudCompraViewSet)
router.register(r'producto',views.SolicitudProductoViewSet)
=======
>>>>>>> 4e8dbca1ea3a1fcb5201a3424a90bf5c3445a249

urlpatterns = [
    path('',include(router.urls))
]
