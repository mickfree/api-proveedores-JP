from django.urls import path,include
from .views import *
from .views import home


urlpatterns = [
    path('', home, name='home'),
]