from django.shortcuts import render
from .models import Producto

def inicio(request):
    return render(request, 'inventario/inicio.html')

def productos(request):
    lista_productos = Producto.objects.all()

    return render(
        request,
        'inventario/productos.html',
        {'productos': lista_productos}
    )
# Create your views here.
