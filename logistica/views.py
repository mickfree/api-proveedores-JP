from django.shortcuts import render
from api.models import *
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
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
        solicitud_list = SolicitudCompra.objects.all().prefetch_related('productos', 'solicitudproducto_set')
        data = []
        for solicitud in solicitud_list:
            if not solicitud.numero:  # Asegúrate de que el número no esté vacío
                continue  # Salta esta solicitud si no tiene número
            productos = []
            for sp in solicitud.solicitudproducto_set.all():
                producto = sp.producto
                productos.append(producto.nombre)
            data.append({
                'numero': solicitud.numero,
                'productos': ', '.join(productos),
                'proveedor': solicitud.proveedor.nombre_empresa,
                'entrega': solicitud.entrega,
                'pago': solicitud.pago,
                'estado': solicitud.estado
            })
        return {'solicitudes': data, 'numero_compra': solicitud_list.count()}

