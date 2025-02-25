from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.views.generic import *
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .forms import ProveedorForm
from api.models import *
import requests

# Implements Cbv's
class HomeProveedoresView(View):
    def get(self, request):
        try:
            proveedores = Proveedor.objects.all()
            numero_proveedores = proveedores.count()
            return render(request, 'proveedores.html', {'numero_proveedores': numero_proveedores, 'proveedores': proveedores})
        except Exception as e:
            return HttpResponse(f"Error al obtener los proveedores: {str(e)}", status=500)

class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedores_form.html'
    success_url = reverse_lazy('home_proveedores')

    def form_valid(self, form):
        self.object = form.save()
        return redirect('home_proveedores')


class DetailProveedorView(DetailView):
    model = Proveedor
    template_name = 'proveedores_detail.html'
    context_object_name = 'proveedor'
   
class EditProveedorView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedores_edit.html'
    
    def get_success_url(self):
        return reverse_lazy('detail_proveedores',kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proveedor'] = self.object
        return context
    
    
class DeleteProveedorView(DeleteView):
    model = Proveedor
    template_name = 'proveedores_delete.html'
    success_url = reverse_lazy('home_proveedores')
    context_object_name = 'proveedor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proveedor'] = self.get_object()
        return context
