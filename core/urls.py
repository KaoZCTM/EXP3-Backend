from django.urls import path
from . import views

urlpatterns=[
    path('', views.Inicio, name="Inicio"),
    path('Inicio/', views.Inicio, name="Inicio"),
    path('Registrate/', views.Registrate, name="Registrate"),
    path('DescipcionAlimentos/', views.DescripcionAlimentos, name="DescripcionAlimentos"),
    path('login/', views.login, name="login"),
    path('Conocenos/', views.Conocenos, name="Conocenos"),
    path('BibliotecaPerros/', views.BibliotecaPerros, name="BibliotecaPerros"),
    path('Biblioteca/', views.Biblioteca, name="Biblioteca"),
]