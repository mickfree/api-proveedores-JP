from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.views.generic import *
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from api.models import *
from django.views.decorators.http import require_POST
from .forms import *

import requests

  
# class HomeStockView(View):
#     def get(self, request):
#         URL_API = "http://localhost:8000/api/v1/stock/"
        
#         response = requests.get(URL_API)
        
#         if response.status_code == 200:
            
#             stocks = response.json()

#              # Obtener IDs de catálogos únicos
#             catalogo_ids = {stock['catalogo'] for stock in stocks}
#             catalogos = Catalogue.objects.filter(id__in=catalogo_ids)
#             catalogo_dict = {catalogo.id: catalogo.nombre for catalogo in catalogos}
            
#             # Añadir nombre del catálogo a cada stock
#             for stock in stocks:
#                 stock['catalogo_nombre'] = catalogo_dict.get(stock['catalogo'], "Desconocido")    

                              
#             sum_stocks = sum(item['cantidad'] for item in stocks)

            
#             return render(request, 'inventario.html', {'sum_stocks': sum_stocks, 'stocks': stocks})
#         else:
#             return HttpResponse("Error al obtener los catálogos", status=500)

class HomeStockView(View):
    def get(self, request):
        URL_API = "http://localhost:8000/api/v1/stock/"
        
        response = requests.get(URL_API)
        
        if response.status_code == 200:
            stocks = response.json()
            
            # Obtener IDs de catálogos únicos
            catalogo_ids = {stock['catalogo'] for stock in stocks}
            catalogos = Catalogue.objects.filter(id__in=catalogo_ids)
            catalogo_dict = {catalogo.id: {'nombre': catalogo.nombre, 'precio': catalogo.precio} for catalogo in catalogos}
            
            # Añadir nombre y precio del catálogo a cada stock
            for stock in stocks:
                catalogo_info = catalogo_dict.get(stock['catalogo'], {"nombre": "Desconocido", "precio": 0})
                stock['catalogo_nombre'] = catalogo_info['nombre']
                # stock['catalogo_precio'] = catalogo_info['precio']
                
            sum_stocks = sum(item['cantidad'] for item in stocks)
            
            return render(request, 'inventario.html', {'sum_stocks': sum_stocks, 'stocks': stocks})
        else:
            return HttpResponse("Error al obtener los catálogos", status=500)



class DetailStockView(DetailView):
    model = Stock
    template_name = 'inventario_detail.html'
    context_object_name = 'stock'
    
    
class StockCreateView(CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'inventario_form.html'
    success_url = reverse_lazy('home_inventario')

    def form_valid(self, form):
        self.object = form.save()
        return redirect('home_inventario')



class EditStockView(UpdateView):
    model = Stock
    form_class = StockForm
    template_name = 'inventario_edit.html'
    
    def get_success_url(self):
        return reverse_lazy('detail_inventario',kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stock'] = self.object
        return context
    