
#an 1B-CREACION DEL "context_processors" PARA LUEGO REGISTRARLO EN "settings.py"

from blog.models import Category, Article #an IMPORTAR LA "class Category" y "class Article" DE "models.py" CORRESPONDIENTE A LA APP CREADA "blog"

def get_categories(request):

    #an REALIZAR CONSULTA A LA BD
    id_Category_in_Article = Article.objects.filter(public=True).values_list('categories', flat=True) #an flat=True SACA LOS RESULTADOS EN TEXTO PLANO
    categories = Category.objects.filter(id__in=id_Category_in_Article).values_list('id', 'name')    #an (SUBCONSULTAS).filter(id__in=id_Category_in_Article) FILTRAR LAS CATEGORIAS CUYO "id" SE ESTEN USANDO EN EL LISTADO DE ARTICULOS (id_Category_in_Article)
                                                                                   #an .values_list('id', 'name') SELECCIONA SOLAMENTE UNO O DOS ELEMENTOS DE LA BD, CON LOS CAMPOS: 'id', 'name'. TODO ESTO PARA QUE NO SE SATURE LA MEMORIA(.all() SATURA LA MEMORIA PORQUE DEVULEVE TODOS LOS ELEMENTOS DE LA BD AL MISMO TIEMPO).

    return {    #an DEVOLVERA UNA TUPLA CON LISTAS. DENTRO DE LAS LISTAS ESTARAN EL 'id','title','slug'
        'categories':categories,
        'ids':id_Category_in_Article
    }