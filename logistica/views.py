from django.shortcuts import render
import requests
from django.http  import HttpResponse, JsonResponse
from api.models import Proveedor  


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

def home(request):
    # URL de tu propia API dentro de tu proyecto
    URL_API = "http://localhost:8000/api/v1/proveedores/"  # Ajusta la URL según corresponda

    # Realizar la solicitud GET a la API
    response = requests.get(URL_API)

    if response.status_code == 200:
        # La solicitud fue exitosa, obtener y devolver los proveedores
        proveedores = response.json()
        
        # Contar el número de proveedores recibidos
        numero_proveedores = len(proveedores)
        
        # Relizar el context  en la funcion
        return render(request, 'home/logistica.html', {'numero_proveedores': numero_proveedores, 'proveedores': proveedores})
    else:
        # Manejo de errores si la solicitud a la API falla
        return HttpResponse("Error al obtener los proveedores", status=500)

def sum_proveedores(request):
    # URL de tu propia API dentro de tu proyecto
    URL_API = "http://localhost:8000/api/v1/proveedores/"  # Ajusta la URL según corresponda

    # Realizar la solicitud GET a la API
    response = requests.get(URL_API)

    if response.status_code == 200:
        # La solicitud fue exitosa, obtener y devolver los proveedores
        proveedores = response.json()
        
        # Contar el número de proveedores recibidos
        numero_proveedores = len(proveedores)
        
        # Devolver una respuesta JSON con el número de proveedores
        return JsonResponse({'numero_proveedores': numero_proveedores})
    else:
        # Manejo de errores si la solicitud a la API falla
        return HttpResponse("Error al obtener los proveedores", status=500)


def obtener_proveedores(request):
    # Obtener todos los proveedores desde la base de datos
    proveedores = Proveedor.objects.all()

    # Crear una lista para almacenar los datos de los proveedores
    proveedores_list = []

    # Iterar sobre los proveedores y agregarlos a la lista
    for proveedor in proveedores:
        proveedor_dict = {
            'id': proveedor.id,
            'nombre_empresa': proveedor.nombre_empresa,
            'ruc': proveedor.ruc,
            'direccion': proveedor.direccion,
            'nombre_contacto': proveedor.nombre_contacto,
            'telefonos': proveedor.telefonos,
            'observaciones': proveedor.observaciones,
        }
        proveedores_list.append(proveedor_dict)

    # Devolver una respuesta JSON con los datos de los proveedores
    return render(request, 'base.html', {'obtener_proveedores': obtener_proveedores})
