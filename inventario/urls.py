
from django.urls import path,include
from .views import *

urlpatterns = [
    path('inventario/', HomeStockView.as_view(), name="home_inventario"),
    path('catalogos/form/',StockCreateView.as_view(), name='form_inventario'),
    path('inventario/detail/<int:pk>/', DetailStockView.as_view() , name='detail_inventario'),
    path('inventario/detail/edit/<int:pk>/', EditStockView.as_view() , name='edit_inventario'),
]
