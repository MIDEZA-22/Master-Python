
#az Importar el Django template
from django import template

#az Cargar la libreria de template
register = template.Library() 

#az Crear los filtros
@register.filter(name='saludo') #r Es un decorador. Es una funcionalidad previa que se le da a un clase o a una funcion

def saludo(nombre):

    largo = ''
    if len(nombre) >= 8:
        largo = '<p>Tu nombre es muy largo</p>'

    return f"<h1 style='background:green;color:white;'>Bienvenido, {nombre} </h1> "+largo