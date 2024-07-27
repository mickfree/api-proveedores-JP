from django.shortcuts import render
import requests
from django.http  import HttpResponse, JsonResponse
from api.models import Proveedor
from django.views import View

# class LogisticaHomeView(View):
#     template_name = 'home/logistica.html'

#     def get(self, request):
#         context = {}
#         context.update(self.get_proveedores_data())
#         context.update(self.get_inventario_data())
#         return render(request, self.template_name, context)

#     def get_proveedores_data(self):
#         proveedores_url = "http://localhost:8000/api/v1/proveedores/"
#         return self.fetch_api_data(proveedores_url, 'proveedores')

#     def get_inventario_data(self):
#         inventario_url = "http://localhost:8000/api/v1/stock/"
#         return self.fetch_api_data(inventario_url, 'stock')

#     def fetch_api_data(self, url, data_type):
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json()
#             return {
#                 f'numero_{data_type}': len(data),
#                 data_type: data
#             }
#         else:
#             return {f'error_{data_type}': f"Error al obtener los {data_type}"}


class LogisticaHomeView(View):
    template_name = 'home/logistica.html'

    def get(self, request):
        context = {}
        context.update(self.get_proveedores_data())
        context.update(self.get_inventario_data())
        context.update(self.get_solicitud_data())
        return render(request, self.template_name, context)

    def get_proveedores_data(self):
        proveedores_url = "http://localhost:8000/api/v1/proveedores/"
        return self.fetch_api_data(proveedores_url, 'proveedores')

    def get_inventario_data(self):
        inventario_url = "http://localhost:8000/api/v1/stock/"
        return self.fetch_api_data(inventario_url, 'stock')
    
    def get_solicitud_data(self):
        solicitud_compras_url = "http://localhost:8000/api/v1/compra/"
        return self.fetch_api_data(solicitud_compras_url, 'compra')

    def fetch_api_data(self, url, data_type):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data_type == 'stock':
                total_quantity = sum(item['cantidad'] for item in data)
                return {
                    'numero_stock': total_quantity,
                    data_type: data
                }
            return {
                f'numero_{data_type}': len(data),
                data_type: data
            }
        else:
            return {f'error_{data_type}': f"Error al obtener los {data_type}"}
