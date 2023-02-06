
#an CREAR URLS EN LA MISMA APP (PARA NO TENER UNA CANTIDAD EXCESIVA DE URLS EN EL "ProyectoDjango")

from django.urls import path #an IMPORTAR "path" PARA DEFINIR NUESTRAS RUTAS
from . import views #an IMPORTAR LA "views" EN LA APP DONDE NOS ENCONTRAMOS (EL PUNTO . SIGNIFICA EL DIRECTORIO ACTUAL). EN ESTE CASO (pages)

#an DEFINIR NUESTRA LISTA DE RUTAS
urlpatterns = [
    path('pagina/<str:slug>', views.page, name="page"),
]
