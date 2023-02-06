from tabnanny import verbose
from django.apps import AppConfig


class MiappConfig(AppConfig):
    name = 'miapp'

    #az PARA VISUALIZAR EL NOMBRE DE MI APP(miapp) CON OTRO NOMBRE, SE COLOCA LO SIGUIENTE:
    verbose_name = "Mi primerta aplicación"
