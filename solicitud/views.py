from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator
from api.models import SolicitudCompra, SolicitudProducto
from decimal import Decimal, ROUND_HALF_UP
from django.forms import modelformset_factory
from .forms import *

def lista_solicitudes_compra(request):
    solicitud_list = SolicitudCompra.objects.all().prefetch_related('productos', 'solicitudproducto_set')
    data = []
    for solicitud in solicitud_list:
        if not solicitud.numero:  # Asegúrate de que el número no esté vacío
            continue  # Salta esta solicitud si no tiene número
        productos = []
        total_con_igv = Decimal('0.00')
        for sp in solicitud.solicitudproducto_set.all():
            producto = sp.producto
            subtotal = sp.cantidad * producto.precio  # Usa producto.precio en lugar de sp.precio_unitario
            igv = subtotal * Decimal('0.18')
            total_producto = subtotal + igv
            total_con_igv += total_producto.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            productos.append({
                'nombre': producto.nombre,
                'cantidad': sp.cantidad,
                'precio': producto.precio,
                'total_con_igv': total_producto
            })
        data.append({
            'numero': solicitud.numero,
            'fecha': solicitud.fecha,
            'productos': productos,
            'proveedor': solicitud.proveedor.nombre_empresa,
            'entrega': solicitud.entrega,
            'pago': solicitud.pago,
            'total_con_igv': total_con_igv,
            'estado': solicitud.estado
        })
    paginator = Paginator(data, 10)  # Muestra 10 solicitudes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lista.html', {'page_obj': page_obj})


def detalle_solicitud_compra(request, numero): #numero
    solicitud = get_object_or_404(SolicitudCompra, numero=numero) #numero
    productos = solicitud.solicitudproducto_set.all()
    
    productos_detalle = []
    for producto in productos:
           precio_sin_igv = producto.producto.precio
           precio_unitario = producto.producto.precio
           total = precio_unitario * producto.cantidad
           igv = (total * Decimal('0.18')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
           precio_con_igv = (total * Decimal('1.18')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
           productos_detalle.append({
               'nombre': producto.producto.nombre,
               'cantidad': producto.cantidad,
               'igv': igv,
               'precio_unitario':precio_unitario,
               'total':total,
               'precio_sin_igv': precio_sin_igv.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
               'precio_con_igv': precio_con_igv.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
             })
    
    total_sin_igv = sum([p['precio_sin_igv'] * p['cantidad'] for p in productos_detalle])
    total_igv = sum([p['igv'] * p['cantidad'] for p in productos_detalle])
    total_con_igv = sum([p['precio_con_igv'] for p in productos_detalle])

    return render(request, 'detalle.html', {
        'solicitud': solicitud,
        'productos': productos_detalle,
        'total_sin_igv': total_sin_igv,
        'total_igv': total_igv,
        'total_con_igv': total_con_igv
    })


def crear_solicitud_compra(request):
    if request.method == 'POST':
        form = SolicitudCompraForm(request.POST)
        if form.is_valid():
            solicitud = form.save()
            productos = form.cleaned_data.get('productos')
            for producto in productos:
                SolicitudProducto.objects.create(
                    solicitud=solicitud,
                    producto=producto,
                    cantidad=1  # Puedes ajustar esto según tus necesidades
                )
            return redirect('lista_solicitudes_compra')  # Asume que tienes esta URL
    else:
        form = SolicitudCompraForm()
    return render(request, 'crear.html', {'form': form})



def add_productos(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudCompra, id=solicitud_id)
    if request.method == 'POST':
        form = AddProductosForm(request.POST)
        if form.is_valid():
            productos = form.cleaned_data['productos']
            solicitud.productos.add(*productos)
            return redirect('detalle_solicitud', solicitud_id=solicitud.id)
    else:
        form = AddProductosForm()
    return render(request, 'add_productos.html', {'form': form, 'solicitud': solicitud})