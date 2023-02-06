"""ProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include #an 1d-INCLUIR LA FUNCION "include" PARA QUE LAS URLS CREADAS EN CADA APP("mainapp" y "pages") FUNCIONEN CORRECTAMENTE
from django.conf import settings #r 2A-INCLUIR EL FICHERO DE "settings" PARA ACCEDER A LAS CONFIGURACIONES REALIZADAS en "settings.py"

urlpatterns = [
    path('admin/', admin.site.urls),

    #an 2d-CARGAR LAS RUTAS DE CADA UNA DE LAS APPS("mainapp", "pages" y "blog")
    path('', include('mainapp.urls')), #an CARGAR LA RUTA DE LA APP(mainapp). '' LA PRIMERA RUTA SE DEJA VACIO PARA QUE SEAN RUTAS LIMPIAS
    path('', include('pages.urls')), #an CARGAR LA RUTA DE LA APP(pages). '' LA PRIMERA RUTA SE DEJA VACIO PARA QUE SEAN RUTAS LIMPIAS
    path('', include('blog.urls')), #an CARGAR LA RUTA DE LA APP(blog). '' LA PRIMERA RUTA SE DEJA VACIO PARA QUE SEAN RUTAS LIMPIAS
]

#r 3A-RUTA DE LAS IMAGENES
if settings.DEBUG: #r Comprueba si estamos en modo DEBUG. Que significa que NO estamos en modo produccion 'DEBUG=True'. Si DEBUG=False ya no hara falta porque la URL de la imagen funcionara directamente
    from django.conf.urls.static import static #r Esto es para tener accecible la funcion static que va permitir pasar la URL de la imagen a un fichero estatico que pueda leer el framework
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #r Lo que se hace con static es cargar el directorio que tenemos que leer y luego la ruta completa