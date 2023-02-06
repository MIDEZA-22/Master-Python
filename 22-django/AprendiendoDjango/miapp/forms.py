from django import forms #az IMPORTAR el forms DE DJANGO PARA CREAR NUESTRO FORMULARIO
from django.core import validators #az IMPORTAR LA LIBRERIA DE VALIDACIONES "validators"

class FormArticle(forms.Form): #az Una clase que hereda de otra clase. Crear un formulario heredando de la clase "forms.Form"
    
    title = forms.CharField(
        label = "Titulo",
        max_length = 20,
        required = True, #az Es necesario completar el campo titutlo por eso el "False"
        widget = forms.TextInput( #az Se crear un widget(artilugio) para especificar que es un TextInput
            #an PRIMERA FORMA PARA DARLE ATRIBUTOS(attrs) AL TextInput con attrs
            attrs = {
                'placeholder':'Ingrese el titulo',
                'class':'titulo_form_article',
            }
        ),
        validators = [  #az Para crear la validaciones, simplemente colocar "validators"
            validators.MinLengthValidator(4, 'El titulo es muy corto'), #az Validar si el titulo tiene como minimo 4 caracteres. Si es asi mostrar el mensaje
            validators.RegexValidator('^[A-Za-z0-9 ]*$', 'El titulo esta mal formado', 'invalid_title') #az Valida expresiones regulares. Desde la A hasta la Z. Desde la "a" hasta la "z". Desde el 0 hasta el 9. El ('^[ ]*$') siginifica que se puede validar infinidad de veces
        ]
    )

    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea, #az Se crear un widget(artilugio) para especificar que es un Textarea
        validators=[
            validators.MaxLengthValidator(20, 'El contenido es muy largo')
        ]
    )

    #an SEGUNDA FORMA PARA DARLE ATRIBUTOS(attrs) AL Textarea con attrs
    content.widget.attrs.update({
        'placeholder':'Ingrese el contenido',
        'class':'contenido_form_article',
        'id':'contenido_form'
    })

    #az Se crea aparte las opciones de SI o NO. Para luego pasarlas
    public_options = [
        (1,'SI'),
        (0,'NO')
    ]

    public = forms.TypedChoiceField( #az TypedChoiceField permite mostrar un campo select y pasandole el "public_options"
        label = "¿Publicado?",
        choices = public_options #az choices(opciones)
    )
    