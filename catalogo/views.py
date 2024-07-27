from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse
from django.views.generic import *
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from api.models import *
from .forms import *
from django.views.decorators.http import require_POST 
from django.forms import *
import requests

# Implements Cbv's
        
class HomeCatalogosView(View):
    def get(self, request):
        URL_API = "http://localhost:8000/api/v1/catalogues/"
        
        response = requests.get(URL_API)
        
        if response.status_code == 200:
            
            catalogos = response.json()
            
            # Obtener IDs de proveedores únicos
            proveedor_ids = {catalogo['proveedor'] for catalogo in catalogos}
            proveedores = Proveedor.objects.filter(id__in=proveedor_ids)
            proveedor_dict = {proveedor.id: proveedor.nombre_empresa for proveedor in proveedores}
            
            # Añadir nombre del proveedor a cada catálogo
            for catalogo in catalogos:
                catalogo['nombre_empresa'] = proveedor_dict.get(catalogo['proveedor'], "Desconocido")
            
            numero_catalogos = len(catalogos)
            
            return render(request, 'catalogo.html', {'numero_catalogos': numero_catalogos, 'catalogos': catalogos})
        else:
            return HttpResponse("Error al obtener los catálogos", status=500)
        

class CatalogueCreateView(CreateView):
    model = Catalogue
    form_class = CatalogueForm
    template_name = 'catalogo_form.html'
    success_url = reverse_lazy('home_catalogos')

    def form_valid(self, form):
        self.object = form.save()
        return redirect('home_catalogos')


class DetailCatalogueView(DetailView):
    model = Catalogue
    template_name = 'catalogo_detail.html'
    context_object_name = 'catalogue'
    

class EditCatalogueView(UpdateView):
    model = Catalogue
    form_class = CatalogueForm
    template_name = 'catalogo_edit.html'
    
    def get_success_url(self):
        return reverse_lazy('detail_catalogo',kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalogue'] = self.object
        return context
    
    
class DeleteCatalogueView(DeleteView):
    model = Catalogue
    template_name = 'catalogo_delete.html'
    success_url = reverse_lazy('home_catalogos')
    context_object_name = 'catalogue'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalogue'] = self.get_object()
        return context
