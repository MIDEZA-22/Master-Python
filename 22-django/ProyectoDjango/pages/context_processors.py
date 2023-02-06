
#an 1c-CREACION DEL "context_processors" PARA LUEGO REGISTRARLO EN "settings.py"

from pages.models import Page #an IMPORTAR LA "class Page" DE "models.py" CORRESPONDIENTE A LA APP CREADA "pages"

def get_pages(request):

    #an REALIZAR CONSULTA A LA BD
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug') #an (PRIMERA CONDICION) .filter(visible=True) SELECIONA SOLAMENTE LOS ELEMENTOS DE LA BD QUE TIENEN EL CAMPO "visible" SELECCIONADO O "True"
                                                                                                   #an (SEGUNDA CONDICION) .values_list('id', 'title', 'slug') SELECCIONA SOLAMENTE UNO O DOS ELEMENTOS DE LA BD, CON LOS CAMPOS: 'id', 'title', 'slug'. TODO ESTO PARA QUE NO SE SATURE LA MEMORIA(.all() SATURA LA MEMORIA PORQUE DEVULEVE TODOS LOS ELEMENTOS DE LA BD AL MISMO TIEMPO).

    return {    #an DEVOLVERA UNA TUPLA CON LISTAS. DENTRO DE LAS LISTAS ESTARAN EL 'id','title','slug'
        'pages':pages
    }