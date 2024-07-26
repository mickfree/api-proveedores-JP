from django.shortcuts import render
import requests
from django.http  import HttpResponse, JsonResponse
from api.models import Proveedor
from django.views import View

# def api_proveedores_home(request):
#     URL_API = "http://localhost:8000/api/v1/proveedores/"  

#     response = requests.get(URL_API)

#     if response.status_code == 200:

#         proveedores = response.json()
        
#         numero_proveedores = len(proveedores)
        
#         return render(request, 'home/logistica.html', {'numero_proveedores': numero_proveedores, 'proveedores': proveedores})
#     else:

#         return HttpResponse("Error al obtener los proveedores", status=500)
    
# def api_inventario_home(request):
    
#     URL_API = "http://localhost:8000/api/v1/stock/"  

#     response = requests.get(URL_API)

#     if response.status_code == 200:

#         stock = response.json()
        
#         numero_stock = len(stock)
        
#         return render(request, 'home/logistica.html', {'numero_stock': numero_stock, 'stock': stock})
#     else:

#         return HttpResponse("Error al obtener los proveedores", status=500)
    
class LogisticaHomeView(View):
    template_name = 'home/logistica.html'

    def get(self, request):
        context = {}
        context.update(self.get_proveedores_data())
        context.update(self.get_inventario_data())
        return render(request, self.template_name, context)

    def get_proveedores_data(self):
        proveedores_url = "http://localhost:8000/api/v1/proveedores/"
        return self.fetch_api_data(proveedores_url, 'proveedores')

    def get_inventario_data(self):
        inventario_url = "http://localhost:8000/api/v1/stock/"
        return self.fetch_api_data(inventario_url, 'stock')

    def fetch_api_data(self, url, data_type):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                f'numero_{data_type}': len(data),
                data_type: data
            }
        else:
            return {f'error_{data_type}': f"Error al obtener los {data_type}"}
