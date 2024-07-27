from django.urls import path
from .views import *
from django.http import HttpResponse



urlpatterns = [
    path('solicitudes/', lista_solicitudes_compra, name='lista_solicitudes_compra'),
    path('solicitudes/crear/', crear_solicitud_compra, name='crear_solicitud_compra'),
    path('solicitudes/<str:numero>/', detalle_solicitud_compra, name='detalle_solicitud_compra'),
    path('solicitud/<int:solicitud_id>/add_productos/', add_productos, name='add_productos'),

]