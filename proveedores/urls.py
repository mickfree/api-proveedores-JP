from django.urls import path,include
from .views import *
# from .views import *


urlpatterns = [
    path('proveedores/', HomeProveedoresView.as_view(), name='home_proveedores'),
    path('proveedores/form/', ProveedorCreateView.as_view(), name='form_proveedores'),
    path('proveedores/detail/<int:pk>/' , DetailProveedorView.as_view(), name='detail_proveedores'),
    path('proveedores/detail/edit/<int:pk>/' , EditProveedorView.as_view(), name='edit_proveedores'),
    path('proveedores/delete/<int:pk>/', DeleteProveedorView.as_view() ,name='delete_proveedores')

]