from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Catalogue)
admin.site.register(Stock)
admin.site.register(SolicitudCompra)
admin.site.register(SolicitudProducto)
