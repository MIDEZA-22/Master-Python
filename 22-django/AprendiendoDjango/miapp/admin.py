from django.contrib import admin
from .models import Article, Category #az El punto . significa para indicar que es un fichero que esta en esta misma carpeta

#r (SEGUNDO ) CREAR LA CONFIGURACION PARA QUE LOS CAMPOS QUE SOLO SE PUEDEN LEER(NO SE PUEDEM MODIFICAR) DENTRO DE ARTICULO (created_at , update_at) SE VISUALICEN DENTRO DEL PANEL DE ADMINISTRACION|ESPECIFICAMENTE DENTRO DE ARTICULO

class ArticleAdmin(admin.ModelAdmin): #az admin.ModelAdmin Es la clase que nos permite manipular estos modelos DENTRO DEL PANEL DE ADMINISTRACION
    readonly_fields = ('created_at', 'update_at') #az readonly_fields(Es una propiedad de la clase admin.ModelAdmin) Sirve para indicar los campos de solo lectura 

#r (PRIMERO) REGISTRAR LOS MODELOS O TABLAS CREADAS EN models.py PARA GENERAR UN CRUD DENTRO PANEL DE ADMINISTRACION

admin.site.register(Article, ArticleAdmin) #az register() es un metodo que permite cargar nuestros modelos (models.py) dentro del PANEL DE ADMINISTRACION
                                           #az Se le pasa como parametro a register la clase creada(ArticleAdmin) para que al generar el CRUD de ARTICULO, se muestren al mismo tiempo los campos de solo lectura(created_at y update_at) 
admin.site.register(Category)

#r CANBIAR EL NOMBRE DEL TITULO DEL PANEL DE ADMINISTRACION (Sitio administrativo) Y EL NOMBRE DE LA PESTAÑA DE LA VENTANA (Sitio administrativo|Sitio de administracion de Django)
#az site sirve para acceder el panel de administracion del sitio
admin.site.site_header = "MIDEZA" #az CAMBIAR EL NOMBRE DEL TITULO DEL PANEL DE ADMINISTRACION
admin.site.site_title = "MIJAIL | PYTHON" #az CAMBIAR EL NOMBRE DE LA PESTAÑA DE LA VENTANA
admin.site.index_title = "Panel de admnistración de MIDEZA" #az CAMBIAR EL SUBTITULO DEL PANEL DE ADMINISTRACION