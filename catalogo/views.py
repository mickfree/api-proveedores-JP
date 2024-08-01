from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.views.generic import *
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from api.models import *
from .forms import *
from django.forms import *
import requests

# Implements Cbv's

class HomeCatalogosView(View):
    def get(self, request):
        try:
            # Obtén todos los catálogos
            catalogos = Catalogue.objects.all()

            # Obtener IDs de proveedores únicos
            proveedor_ids = catalogos.values_list('proveedor_id', flat=True).distinct()
            proveedores = Proveedor.objects.filter(id__in=proveedor_ids)
            proveedor_dict = {proveedor.id: proveedor.nombre_empresa for proveedor in proveedores}

            # Añadir nombre del proveedor a cada catálogo
            catalogos_list = []
            for catalogo in catalogos:
                catalogo_dict = {
                    'id': catalogo.id,
                    'nombre': catalogo.nombre,
                    'proveedor': catalogo.proveedor_id,
                    'nombre_empresa': proveedor_dict.get(catalogo.proveedor_id, "Desconocido"),
                    'precio': catalogo.precio,  
                    'descripcion': catalogo.descripcion
                }
                catalogos_list.append(catalogo_dict)

            numero_catalogos = len(catalogos_list)

            return render(request, 'catalogo.html', {'numero_catalogos': numero_catalogos, 'catalogos': catalogos_list})
        except Exception as e:
            return HttpResponse(f"Error al obtener los catálogos: {str(e)}", status=500)

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
