from django.shortcuts import render
from .models import Page #an IMPORTAR LOS MODELOS PARA HACER CONSULTASA A LA BD

from django.contrib.auth.decorators import login_required #R USAR DECORADORES DE AUTENTICACION PARA QUE LOS USUARIOS NO AUTENTICADOS NO PUEDAN ENTRAR A NINGUN ENLACE (UN DECORADOR HACE UNA FUNCIONALIDAD PREVIA A LA EJECUCION DEL CODIGO DE LA VISTA)

# Create your views here.
@login_required(login_url="login") #R DECORADOR
def page(request, slug):

    page = Page.objects.get(slug=slug) #an OBTENER TODOS LOS REGISTROS DE LA BD CON LA CONDICION QUE EL 'slug' DE LA BD SE IGUAL AL 'slug' QUE VIENE DE LA URL

    return render(request, "pages/page.html", {
        "page": page,
    })