
#R CREACION DEL FORMULARIO BASADA EN EL MODELO "User" PARA LA AUTENTICACION DE LA PAGINA

from django import forms #an IMPORTAR EL MODULO DE FORMULARIOS DE DJANGO
from django.core import validators #an IMPORTAR EL MODULO DE VALIDACIONES

from django.contrib.auth.forms import UserCreationForm #an IMPORTAR EL FORMULARIO POR DEFECTO
from django.contrib.auth.models import User #an IMPORTAR EL MODELO DE USUARIO

class RegisterForm(UserCreationForm): #an La class RegisterForm va a heredar de otra class llamada UserCreationForm
    #an La creacion del Form se hara de manera AUTOMATICA, utilizando un modelo
    class Meta:
        model = User #an El modelo Form va a tomar como referencia al modelo de User
        #an CAMPOS QUE VA A UTILIZAR EL FORM
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']