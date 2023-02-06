from tabnanny import verbose
from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'pages'

    #an 1a-CAMBIAR EL NOMBRE DE LA APP(PAGES) DENTRO DEL PANEL DE ADMINISTRACION, LUEGO CODIFICAR DENTRO DE: settings.py
    verbose_name ='Gestión de paginas'
