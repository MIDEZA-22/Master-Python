from django.db import models
from ckeditor.fields import RichTextField #an 1f-IMPORTAR "RichTextField" PARA USAR EL EDITOR DE TEXTO ENRIQUECIDO, LUEGO REGISTRARLO EN "settings.py"
from django.forms import ImageField 

from django.contrib.auth.models import User #an 1g-IMPORTAR EL MODELO "User" QUE VIENE POR DEFECTO EN DJANGO, SERVIRA PARA HACER RELACIONES CON "User"

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    #an CAMBIAR LOS NOMBRES QUE ESTAN EN LA LISTA DE "Categorias". TODO EL LISTADO QUE ESTA DENTRO DE "Categorias" SE VISUALIZARA CON EL "name" QUE SE LE PUSO AL CREARLO
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    content = RichTextField(verbose_name='Contenido') #an 2f-USAR SOLO EL OBJETO IMPORTADO RichTextField.ESTO DEBIDO A QUE ES UN OBJETO COMPLETO, POR LO QUE NO NECESITA QUE SE LE ANTECEDA EL "models."
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to="articles") #an SE LE PONE default='null' PORQUE NO ES OBLIGATORIO QUE EL CAMPO CONTENGA SI O SI UNA IMAGEN | upload_to="articles" CREA UNA CARPETA DE MANERA AUTOMATICA LLAMADA 'articles' DENTRO DE LA CARPETA 'media', PREVIAMENTE SE TIENE QUE CREAR LA CARPETA "media" Y REALIZAR LAS CONFIGURACIONES
    public = models.BooleanField(verbose_name='¿Publicado?')
    #an CREAR RELACIONES CON EL MODELO IMPORTADO QUE VIENE POR DEFECTO "User" Y EL MODELO CREADO "Category"
    user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE, editable=False) #an 2g-USAR EL "User" IMPORTADO. DENTRO DEL CAMPO "user" SE VA A GUARDAR EL "ID" DEL USUARIO QUE HA CREADO EL ARTICULO. LA RELARCION DE "Article" con "user" ES DE 1 A 1 (UN ARTICULO A SIDO CREADO POR UN USUARIO)| EL "on_delete=models.CASCADE" SIRVE PARA CUANDO SE BORRE UN USUARIO QUE TIENE ARTICULOS, TAMBIEN SE BORREN TODOS SUS REGISTROS VINCULADOS AL USUARIO | 'editable=False' SIRVE OCULTAR EL CAMPO DE 'Usuario' EN EL PANEL DE ADMINISTRACION 
    categories = models.ManyToManyField(Category, verbose_name='Categorias', blank=True) #an LA RELACION DE "Article" con "categories" ES DE MUCHOS A MUCHOS (MUCHOS ARTICULOS PUEDEN TENER MULTIPLES CATEGORIAS) | SE LE PONE "blank=True" PARA NO ESTAR OBLIGADOS A INTRODUCIR UNA CATEGORIA
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado el')

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['-created_at'] #an ORDENAR LOS ARTICULOS DESDE EL MAS NUEVO AL MAS VIEJO

    #an CAMBIAR LOS NOMBRES QUE ESTAN EN LA LISTA DE "Articulos". TODO EL LISTADO QUE ESTA DENTRO DE "Articulos" SE VISUALIZARA CON EL "title" QUE SE LE PUSO AL CREARLO
    def __str__(self):
        return self.title