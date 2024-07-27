from django.urls import path,include
from .views import *
# from .views import home


urlpatterns = [
    path('', LogisticaHomeView.as_view(), name='api_home'),
    
]


