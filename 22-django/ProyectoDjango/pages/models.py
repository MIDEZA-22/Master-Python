from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField #an 1e-IMPORTAR "RichTextField" PARA USAR EL EDITOR DE TEXTO ENRIQUECIDO, LUEGO REGISTRARLO EN "settings.py"

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido') #an 2e-USAR SOLO EL OBJETO IMPORTADO RichTextField.ESTO DEBIDO A QUE ES UN OBJETO COMPLETO, POR LO QUE NO NECESITA QUE SE LE ANTECEDA EL "models."
    slug = models.CharField(unique=True ,max_length=150, verbose_name='URL amigable')
    order = models.IntegerField(default=0, verbose_name='Orden')
    visible = models.BooleanField(verbose_name='¿Visible?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    #an CAMBIAR LOS NOMBRES QUE ESTAN EN LA LISTA DE "Páginas". TODO EL LISTADO QUE ESTA DENTRO DE "Paginas" SE VISUALIZARA CON EL "title" QUE SE LE PUSO AL CREARLO
    def __str__(self):
        return self.title