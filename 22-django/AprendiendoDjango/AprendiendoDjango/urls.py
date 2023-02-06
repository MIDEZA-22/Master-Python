"""AprendiendoDjango URL Configuration

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
from distutils.debug import DEBUG
from django.contrib import admin
from django.urls import path

from django.conf import settings #az Importar los settings para acceder a la configuracion con respecto a la imagen que se hizo (#Media files)

#ro Importar app con mis vistas

from miapp import views
# import miapp.views #az Otra forma de importar. Se utilizaria miapp.views

urlpatterns = [
    #az path('nombre de la ruta/', funcion a ejecutar, identificador(name) servira para hacer redirecciones)
    path('admin/', admin.site.urls),
    path('',views.index, name="index"), #az Las comillas simples vaicas '' significan que sera la pagina principal
    path('inicio/',views.index, name='inicio'),
    path('hola-mundo/',views.hola_mundo, name='hola_mundo'),
    path('pagina-pruebas/',views.pagina, name='pagina'),

    path('pagina-pruebas/<int:redirigir>',views.pagina, name='pagina'),

    #az <str:nombre>/ => Sirve para pasar como parametro a la URL un nombre
    #az SE CREAN TODOS LOS CASOS POSIBLES PARA QUE FUNCIONEN LOS PARAMETROS OPCIONALES
    path('contacto-dos/', views.contacto, name='contacto'), #az CASO 1: sin ningun parametro para la URL
    path('contacto-dos/<str:nombre>/', views.contacto, name='contacto'), #az CASO 2: Solo un parametro para la URL <str:nombre>/
    path('contacto-dos/<str:nombre>/<str:apellidos>/', views.contacto, name='contacto'), #az CASO 3: Con dos parametros para la URL <str:nombre>/<str:apellidos>/
    
    path('crear-articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name="crear_articulo"),

    path('articulo/', views.articulo, name='articulo'),

    path('editar-articulo/<int:id>', views.editar_articulo, name='editar_articulo'),

    path('articulos/', views.articulos,name='articulos'),

    path('borrar_articulo/<int:id>', views.borrar_articulo, name='borrar'),

    path('save-article/', views.save_article, name='save'),

    path('create-article/', views.create_article, name='create'),

    path('create-full-article/', views.create_full_article, name="create_full"),
]

#r CONFIGURACION PARA CARGAR IMAGENES
if settings.DEBUG: #az Comprueba si estamos en modo DEBUG. Que significa que NO estamos en modo produccion 'DEBUG=True'. Si DEBUG=False ya no hara falta porque la URL de la imagen funcionara directamente
    from django.conf.urls.static import static #az Esto es para tener accecible la funcion static que va permitir pasar la URL de la imagen a un fichero estatico que pueda leer el framework
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #az Lo que se hace con static es cargar el directorio que tenemos que leer y luego la ruta completa