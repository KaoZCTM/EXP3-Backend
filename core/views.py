from django.shortcuts import render, redirect
#from .models import Categoria, Vehiculo esto es para las clases
#from .forms import VehiculoForm para las clases

# Create your views here.
def Inicio(request):
    return render(request, 'Inicio.html')

def login(request):
    return render(request, 'login.html')

def Registrate(request):
    return render(request, 'Registrate.html')

def DescripcionAlimentos(request):
    return render(request, 'DescripcionAlimentos.html')

def Conocenos(request):
    return render(request, 'Conocenos.html')

def BibliotecaPerros(request):
    return render(request, 'BibliotecaPerros.html')

def Biblioteca(request):
    return render(request, 'Biblioteca.html')


























#funciones para las clases

# def productos(request):
#     datos = Vehiculo.objects.all()              #similar a select * from Vehiculo
#     return render(request, 'productos.html',{"datos":datos})

# def crear(request):
#     if request.method=='POST':
#         vehiculoform = VehiculoForm(request.POST, request.FILES)
#         if vehiculoform.is_valid():
#             vehiculoform.save()         #similar al insert into
#             return redirect ('productos')
#     else:
#         vehiculoform = VehiculoForm()
#     return render (request, 'crear.html', {'vehiculoform': vehiculoform })