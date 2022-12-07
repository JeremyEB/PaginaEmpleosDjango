from django.urls import path

from PaginaEmpleosApp import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('Programacion', views.Programacion, name="Programacion"),
    path('DiseñadorTIC', views.DiseñadorTIC, name="DiseñadorTIC"),
    path('Ciberseguridad', views.Ciberseguridad, name="Ciberseguridad"),
    path('Mecatronica', views.Mecatronica, name="Mecatronica"),
    path('IA', views.IA, name="IA"),
    path('Admin', views.Admin, name='Admin')
]