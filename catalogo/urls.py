from django.urls import path,include
from .views import *
from .views import *

urlpatterns = [
    path('catalogos/', HomeCatalogosView.as_view(), name='home_catalogos'),
    path('catalogos/form/',CatalogueCreateView.as_view(), name='form_catalogo'),
    path('catalogos/detail/<int:pk>/', DetailCatalogueView.as_view(), name='detail_catalogo'),
    path('catalogos/detail/edit/<int:pk>/', EditCatalogueView.as_view(),name='edit_catalogo'),
    path('proveedores/delete/<int:pk>/', DeleteCatalogueView.as_view() ,name='delete_catalogo')

]


# urlpatterns = [
#     path('proveedores/', HomeProveedoresView.as_view(), name='home_proveedores'),
#     path('proveedores/form/', ProveedorCreateView.as_view(), name='form_proveedores'),
#     path('proveedores/detail/<int:pk>/' , DetailProveedorView.as_view(), name='detail_proveedores'),
#     path('proveedores/detail/edit/<int:pk>/' , EditProveedorView.as_view(), name='edit_proveedores'),
#     path('proveedores/delete/<int:pk>/', DeleteProveedorView.as_view() ,name='delete_proveedores')

# ]