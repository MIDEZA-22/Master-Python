from django.db import models #az IMPORTAR LOS MODELOS DE DJANGO

#r Un MODELO representa una tabla de la BD o un REGISTRO CONCRETO dentro de una TABLA CONCRETA
#r La class Article y Category(modelos) representan las tablas de la BD
#r Lo que se encuentra adentro de la class son columnas de la tabla

# Create your models here.

class Article(models.Model): #az models.Model Indica que es MODELO y no un OBJETO. Que herede de models el Model 
    title = models.CharField(max_length=150, verbose_name="Titulo") #az .CharField es un campo de texto corto
    content = models.TextField(verbose_name="Contenido") #az .TextField es un campo de texto mas amplio
    image = models.ImageField(default='null', verbose_name="Imagen", upload_to="articles") #az upload_to="articles" Sirve para crear una carpeta dentro de "media" para guardar las imagenes
    public = models.BooleanField(verbose_name="¿PUBLICADO?") #az .BooleanField sirve para indicar si el articulo esta publicado o no
    created_at = models.DateTimeField(auto_now_add=True) #az .DateTimeField(auto_now_add=True) sirve para guardar la fecha de creacion en el formato mas completo 
    update_at = models.DateTimeField(auto_now=True) #az .DateTimeField(auto_now=True) sirve para guardar la fecha de edicion en el formato mas completo

    #az CONFIGURAR "Article" PARA VER LOS CAMBIOS DENTRO DEL PANEL DE ADMINISTRACION
    class Meta:
        verbose_name = "Articulo" #az verbose_name Permite colocar el nombre de la "class Article" en singular y en español. Para visualizarlo en el PANEL DE ADMINISTRACION
        verbose_name_plural = "Articulos" #az verbose_name_plural Coloca un nombre plural a un regitro o aun objeto
        ordering = ['-id'] #az Cambiar la ordenacion de los articulos dentro del PANEL DE ADMINISTRACION de forma descendente(-)

    #az CAMBIAR EL NOMBRE DE LOS ARTICULOS POR DEFECTO(Article object (55)) DENTRO DEL PANEL DE ADMINISTRACION

    def __str__(self):
        return f"{self.title} creado el {self.created_at} ({self.public})"

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    #az CONFIGURAR "Category" PARA VER LOS CAMBIOS DENTRO DEL PANEL DE ADMINISTRACION
    class Meta:
        verbose_name = "Categoria" 
        verbose_name_plural = "Categorias"

#R DENTRO DE LAS CLASES (TABLAS) HAY CAMPOS(title, content, image, etc.). CADA CAMPO POSEE ATRIBUTOS. TAN BIEN SE PUEDE PONER EL "verbose_name" PARA PONERLO EN ESPAÑOL