from django.db import models
from distutils.command.upload import upload

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria =  models.CharField(max_length=50, verbose_name='Nombre de Categoria')

    def __str__(self):
        return self.nombreCategoria

class Vehiculo(models.Model):
    idVehiculo = models.CharField(primary_key=True, max_length=10, verbose_name='Id Vehiculo')
    marca = models.CharField(max_length=40, verbose_name='Marca')
    modelo = models.CharField(max_length=40, verbose_name='Modelo')
    imagen = models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen')
    categoria = models.ForeignKey ('Categoria', default=1, on_delete=models.CASCADE, verbose_name='Categoria')

    def __str__(self):
        return self.idVehiculo