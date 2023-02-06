from django.shortcuts import render, get_object_or_404 #M 1C-get_object_or_404 SIRVE PARA MOSTRAR UNA PAGINA 404
from .models import Category, Article #an IMPORTAR LOS MODELOS PARA HACER CONSULTASA A LA BD
from django.core.paginator import Paginator #az AAA-IMPORTAR "Paginator" PARA REALIZAR LA PAGINACION DE LA PAGINA

from django.contrib.auth.decorators import login_required #R USAR DECORADORES DE AUTENTICACION PARA QUE LOS USUARIOS NO AUTENTICADOS NO PUEDAN ENTRAR A NINGUN ENLACE (UN DECORADOR HACE UNA FUNCIONALIDAD PREVIA A LA EJECUCION DEL CODIGO DE LA VISTA)

# Create your views here.
@login_required(login_url='login') #R DECORADOR
def list(request):

    articles = Article.objects.all() #an OBTENER TODOS LOS REGISTROS DE LA BD

    #az AAA-REALIZAR LA PAGINACION DE LA PAGINA
    paginator = Paginator(articles, 2) #az Significa que habra 2 articulos por pagina
    #az AAA-RECOGER NUMERO PAGINA
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, "articles/list.html", {
        'title': 'Artículos',
        'articles': page_articles,
    })

@login_required(login_url='login') #R DECORADOR
def category(request,category_id):
    
    category = get_object_or_404(Category, id=category_id) #M 2C-EN CASO SE LE PASE COMO PARAMETRO UN "id" ERRONERO, MOSTRARA UNA PAGINA 404
    articles = Article.objects.filter(categories=category_id)

    return render(request, 'categories/category.html',{
        "category": category,
        "articles": articles,
    })

@login_required(login_url='login') #R DECORADOR
def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html',{
        "article": article
    })