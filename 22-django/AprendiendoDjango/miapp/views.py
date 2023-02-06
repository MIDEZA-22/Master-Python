from django.shortcuts import render, HttpResponse, redirect #az HttpResponse sirve para dar respuesta http y redirect sirve para redirigir 
from miapp.models import Article #az Importar la tabla Article
from django.db.models import Q #az Sirve para utiliza la tuberia ( | = OR) para hacer consultas a la BD O models
from miapp.forms import FormArticle #az Importar la class FormArticle para trabajar con el formulario que se creo hay
from django.contrib import messages #az Importar libreria para los MENSAJES FLASH(Son mensajes que duran una sesion o muestra un mensaje que dura solo un instante)

# Create your views here
#ro MVC = Modelo Vista Controlador -> Acciones (metodos)
#ro MVT = Modelo Template Vista  -> Acciones (metodos) DJANGO

layout = """
<h1>Sitio web con Django | MIDEZA</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Pagina de pruebas</a>
    </li>
    <li>
        <a href="/contacto-dos">Contacto</a>
    </li>
</ul>
<hr/>
"""


def index(request): #az request es un parametro que permite recibir datos de peticiones que se hague al URL(Parametros, datos, etc.)
    """
    html = ""
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
        ""

    year = 2021
    while year <= 2050:

        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"

        year +=1
        
    html += "</ul>"
    """
    year = 2021
    hasta = range(year, 2051)

    nombre = "MIDEZA"
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C']

    return render(request,'index.html', {
        'title':'Inicio 2',
        'mi_variable':'Soy un dato que está en la vista',
        'nombre':nombre,
        'lenguajes':lenguajes,
        'years': hasta
    }) #az request, 'Vincular a la plantilla(template)', {Se pasa un diccionario o variable con la información}

def hola_mundo(request): 
    return render(request,'hola_mundo.html') #az Vincular a la plantilla(template)

def pagina(request, redirigir=0):

    if redirigir == 1:
        # return redirect('/contacto/mijail/zavala') #az Se coloca redirect para redirigir a URL (http://127.0.0.1:8000/contacto/mijail/zavala/)
        return redirect('contacto', nombre="Mijail", apellidos="Zavala") #az La mejor forma de hacer redireccion EVITANDO ERRORES. Por mas que se cambie la direccion de la URL en urls.py(contacto a contact-dos) ya no afectara.Porque aqui ya no utila el nombre de la URL sino el name='contacto'

    return render(request,'pagina.html',{
        'texto':'Esta es mi lista',
        'lista':['uno','dos','tres']
    }) #az Vincular a la plantilla(template)

def contacto(request, nombre="", apellidos=""): #az Para que los PARAMETROS OPCIONALES funcionen. Se crea rutas con cada CASO posible en la urls.py => Una ruta sin nada, otra con el nombre solo. Y otra con el nombre y apellidos.
    html=""
    if nombre and apellidos:
        html += "<p>El nombre compelto es: </p>"
        html += f"<h3>{nombre} {apellidos}</h3>"
    
    return HttpResponse(layout+"<h2>Contacto</h2>"+html) #az HttpResponse brinda una respuesta http
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
#r Crear un registro dentro de la tabla Article en la BD db.sqlite3(SIN FORMULARIO / CON FORMULARIO(SIN CLASS / CON CLASS)). Importar los MODELOS "from miapp.models import Article" 

    #an SIN FORMULARIO 

def crear_articulo(request,title, content, public):
    articulo = Article( #az Crear una variable con el objeto importado Article(tabla Article de la BD)
        title = title,
        content = content,
        public = public
    )

    articulo.save() #az Guardar los cambios en la BD

    return HttpResponse(f"Artículo creado: <strong>{articulo.title}</strong> - {articulo.content}")

    #an CON FORMULARIO SIN CLASS

        #an 1-CREAR VISTA PARA ALOJAR EL FORMULARIO CREADA EN LA TEMPLATE create_article.html

def create_article(request):

    return render(request, 'create_article.html')

""" 
        #an 2.1-RECEPCION DE DATOS POR EL METODO GET

def save_article(request):
    
    if request.method == 'GET':
        
        title = request.GET['title']
        content = request.GET['content']
        public = request.GET['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )   
    
        articulo.save() #az Guardar los cambios en la BD
    
        return HttpResponse(f"Artículo creado: <strong>{articulo.title}</strong> - {articulo.content}")

    else:

        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")
""" 

        #an 2.2-RECEPCION DE DATOS POR EL METODO POST
    
def save_article(request):
    
    if request.method == 'POST':
        
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )   
    
        articulo.save() #az Guardar los cambios en la BD
    
        return HttpResponse(f"Artículo creado: <strong>{articulo.title}</strong> - {articulo.content}")

    else:

        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")

    #an CON FORMULARIO CON CLASS(forms.py)

        #an 1-CREAR VISTA, PARA ALOJAR EL FORMULARIO CREADA DENTRO DE forms.py LLAMADA FormArticle | PRIMERO IMPORTAR LA CLASE FormArticle

def create_full_article(request):

    #R SEGUNDO SE EJECUTARA EL IF | COMO YA SE HIZO CLICK EN EL ENLACE "Crear articulo-CON CLASS" se mostrara el FORMULARIO O form vacio AUTOMATICAMENTE. CON EL FORMULARIO YA MOSTRADO EN LA PANTALLA, SE PUEDE PROCEDER A RELLENAR LOS CAMPOS PARA SER EVALUADOS POR LAS CONDICIONES Y POSTERIORMENTE SER REDIRIGIDO A LA VISTA DE articulos
    if request.method == 'POST': #az Evalua si la consula es por el metodo 'POST'
        
        formulario = FormArticle(request.POST) #az "request.POST" recoge la lista con todos los datos que llega por el 'POST'  

        if formulario.is_valid(): #az Comprobar si el formulario es valido
            
            data_form = formulario.cleaned_data #az "formulario.cleaned_data" son los datos limpios que llego por el 'POST'

            titulo = data_form.get('title') #az Con el metodo "get()" se puede recoger datos
            contenido = data_form['content'] #az Usando los [] tan bien se recogen los datos, porque 'POST' contiene una lista  
            publico = data_form['public'] #az Usando los [] tan bien se recogen los datos, porque 'POST' contiene una lista

            articulo = Article(
            title = titulo,
            content = contenido,
            public = publico
            )   

            articulo.save() #az Guardar los cambios en la BD

            #az CREAR MENSAJE FLASH(Sesion que solo se muestra 1 vez) | Importar primero la primero la libreria "from django.contrib import messages"
            messages.success(request, f'Se ha creado correctamente el articulo {articulo.id}')
            
            #t return HttpResponse(articulo.title+'-'+articulo.content+'-'+str(articulo.public)) #az SE PUSO ESTO PARA SABER QUE SE HA GUARDA LOS DATOS EN LA BD
            return redirect('articulos') 

    #R PRIMERO SE EJECUTARA EL ELSE | PORQUE CUANDO SE HACE CLICK EN EL ENLACE "Crear articulo-CON CLASS" SOLO SE HIZO CLICK PRIMERO Y NO SE ESCRIBIO NADA. ES POR ESO QUE AUTOMATICAMENTE SE CARGARA EL FORMULARIO VACIO O el form vacio  
    else: 
        formulario = FormArticle()

    return render(request,'create_full_article.html',{
        'form':formulario 
    })

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#an OBTENER UN REGISTRO DE LA BD db.sqlite3

def articulo(request):
    
    try:
        #az Consulta a la BD db.sqlite3
        articulo = Article.objects.get(title="Primer articulo", public=True) #az objects significa accede al modelo, accede a sus objetos 
        respuesta = f"Articulo: {articulo.id}. {articulo.title}"
        
    except:
        respuesta = "Articulo no encontrado"

    return HttpResponse(respuesta)
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#an ACTUALIZAR UN REGISTRO DE LA BD db.sqlite3

def editar_articulo(request, id):
    
    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Artículo {articulo.id} actualizado: <strong>{articulo.title}</strong> - {articulo.content}")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#an LISTAR REGISTROS DE LA BD db.sqlite3

def articulos(request):

    #r Una de las características más poderosas de Django es su Mapeo Relacional de Objetos (ORM), que le permite interactuar con su base de datos, como lo haría con instrucciones SQL (Structured Query Language)

    #articulos = Article.objects.order_by('-id')[3:5] #az el metodo order_by() saca todos los registros de la BD. Si se le pasa un parametro - lo ordenara de forma descendente
                                                      #az [:3] significa que solo mostrara 3 elementos (limit)

    articulos = Article.objects.filter(public=True).order_by('-id') #az Article.objects.all() saca todos los registros de la BD
    """
    #an El metodo filter() permite meter condiciones o puede ir vacio | filter(title="articulo"), filter(title="articulo", id=3), filter()
    #an LOOKUPS | (columna de la BD)__(lookups) 
    #an (title__contains="articulo") saca de la lista al title que contiene la palabra "articulo" | (title__exact="articulo") saca de la lista los que tienen SOLO la palabra "articulo" | (title__iexact) saca de la lista todos los que tienen solo la palabra "articulo" o "Articulo" (No tiene CASE-SENSITIVE)
    #an (id__gt=9) saca de la lista a todos los id mayores que 9 | (id__gte=9) saca de la lista a todos los id mayores o iguales que 9 | (id__lt=9) saca de la lista a todos los id menores que 9 | (id__lte=9) saca de la lista a todos los id menores o iguales que 9
    #an Se puede ingresar mas de una condicion al metodo filter() | (id__lte=9, title__contains="articulo")
    articulos = Article.objects.filter(id__lte=9, title__contains="articulo") #az la coma (,) es como si fuera un AND 
    #articulos = Article.objects.filter(Q(id__lte=9)|Q(title__contains="articulo")) #az la tuberia (|) es como si fuera un OR, PERO SE TIENE QUE IMPORTAR "from django.db.models import Q"

    
    articulos = Article.objects.filter(title="Articulo").exclude(public=False) #az selecciona de la lista a todos los que tienen el nombre de "Articulo" tal cual y quita(excluye) de la lista a los public que tienen como valor True
  
    articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo 2' AND public=0") #az se puede hacer tambien consultas de SQL directamente 
    """

    return render(request,'articulos.html',{
        'articulos': articulos
    })

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#an BORRAR REGISTROS DE LA BD db.sqlite3

def borrar_articulo(request,id):
    
    articulo = Article.objects.get(pk=id)

    articulo.delete()

    return redirect('articulos')
