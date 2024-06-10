from django import forms 
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget
from .models import Categoria, Vehiculo

# class VehiculoForm(forms.ModelForm):
#     class Meta: 
#         model=Vehiculo
#         fields=['idVehiculo', 'marca', 'modelo', 'categoria', 'imagen']
#         labels={
#             'idVehiculo': 'Id Vehiculo',
#             'marca': 'Marca',
#             'modelo': 'Modelo',
#             'categoria': 'Categoria',
#             'imagen': 'Imagen'
#         }
#         widgets={
#             'idVehiculo': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder':'Ingrese Id Vehiculo',
#                     'id':'idvehiculo'
#                 }
#             ),
#             'marca': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder':'Ingrese marca Vehiculo',
#                     'id':'marca'
#                 }
#             ),
#             'modelo': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder':'Ingrese modelo Vehiculo',
#                     'id':'modelo'
#                 }
#             ),
#             'categoria': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'id':'categoria'
#                 }
#             ),
#             'imagen': forms.FileInput(
#                 attrs={
#                     'class': 'form-control',
#                     'id':'imagen'
#                 }
#             )
#         }

