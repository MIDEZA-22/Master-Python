
#an CREAR URLS EN LA MISMA APP (PARA NO TENER UNA CANTIDAD EXCESIVA DE URLS EN EL "ProyectoDjango")

from django.urls import path #an IMPORTAR "path" PARA DEFINIR NUESTRAS RUTAS
from . import views #an IMPORTAR LA "views" EN LA APP DONDE NOS ENCONTRAMOS (EL PUNTO . SIGNIFICA EL DIRECTORIO ACTUAL). EN ESTE CASO (mainapp). 

#an DEFINIR NUESTRA LISTA DE RUTAS
urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),

    path('registro/', views.register_page, name="register"), #m URL para el registro de usuarios
    path('login/', views.login_page, name="login"),#m URL para el login de usuarios
    path('logout/', views.logout_user, name="logout") #m URL para cerra seción
]
