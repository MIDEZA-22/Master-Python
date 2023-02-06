from re import search
from django.contrib import admin
from .models import Page #an 1b-IMPORTAR LA "class Page" DE "models.py" CORRESPONDIENTE A LA APP CREADA "pages"

#an CONFIGURACIONES EXTRAS PARA EL PANEL DE ADMINISTRACION CON RESPECTO A LA APP "pages" PARA LUEGO AGREGAR EL "PageAdmin" AL 2b
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at') #az Mostrar campos de solo lectura
    search_fields = ('title', 'content') #az Mostrar un buscador
    list_filter = ('visible',) #az Filtrar con respecto al campo 'visible'
    list_display = ('title', 'visible', 'created_at') #az Se muestra una tabla con las columnas correspondientes
    ordering = ('created_at',) #az Criterio de ordenacion por defecto

#an 2b-REGISTRAR EL MODELO CREADO EN "models.py" CON EL NOMBRE DE "class Page" PARA VISUALIZARLO EN EL PANEL DE ADMINISTRACION
admin.site.register(Page, PageAdmin)

#an  CAMBIAR EL NOMBRE DE: TITULO GENERAL, LA PESTAÑA Y SUBTITULO DEL PANEL DE ADMINISTRACION RESPECTIVAMENTE
admin.site.site_header = "PROYECTO"
admin.site.site_title = "MIDEZA"
admin.site.index_title = "Panel de gestión"

