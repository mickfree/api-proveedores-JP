from django.urls import path,include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register(r'proveedores',views.ProveedorViewSet)
router.register(r'catalogues', views.CatalogueViewSet)
router.register(r'stock',views.StockViewSet)
router.register(r'compra',views.SolicitudCompraViewSet)
router.register(r'producto',views.SolicitudProductoViewSet)

urlpatterns = [
    path('',include(router.urls))
]
