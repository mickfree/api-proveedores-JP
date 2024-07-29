from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse
from api.models import *
from django.views import View
   
class LogisticaHomeView(View):
    template_name = 'home/logistica.html'

    def get(self, request):
        context = {}
        context.update(self.get_proveedores_data())
        context.update(self.get_inventario_data())
        context.update(self.get_solicitud_data())
        return render(request, self.template_name, context)

    def get_proveedores_data(self):
        proveedores = Proveedor.objects.all()
        return {
            'numero_proveedores': proveedores.count(),
            'proveedores': list(proveedores.values())
        }

    def get_inventario_data(self):
        stock = Stock.objects.all()
        total_quantity = sum(item.cantidad for item in stock)
        return {
            'numero_stock': total_quantity,
            'stock': list(stock.values())
        }

    def get_solicitud_data(self):
        solicitudes = SolicitudCompra.objects.all()
        return {
            'numero_compra': solicitudes.count(),
            'compra': list(solicitudes.values())
        }

