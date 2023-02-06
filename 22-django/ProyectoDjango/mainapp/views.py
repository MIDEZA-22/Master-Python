from django.shortcuts import render, redirect
from django.contrib import messages #an IMPORTAR EL MODULO messages PARA USAR LOS MENSAJES FLASH
from django.contrib.auth.forms import UserCreationForm #an IMPORTAR EL MODULO DE FORMULARIO POR DEFECTO PARA LA AUTENTICACION, EN CASO SE USE
from .forms import RegisterForm #an BBB-IMPORTAR EL FORMULARIO CREADO(RegisterForm) EN BASE AL MODELO 'User'
from django.contrib.auth import authenticate, login, logout #an CCC-IMPORTAR LOS MODULOS DE AUTENTICACION PARA HACER EL LOGIN

# Create your views here.

def index(request):

    return render(request, 'mainapp/index.html',{
        'title':'Inicio'
    })


def about(request):

    return render(request, 'mainapp/about.html',{
        'title':'Sobre nosotros'
    })

#m METODO PARA REGISTRARSE
def register_page(request):

    #R NO MOSTRAR EL ENLACE DE "Registro" CUANDO YA SE ESTA REGISTRADO (O YA NO SE PUEDA INGRESAR POR LA URL CUANDO SE PONGUE ASI: http://127.0.0.1:8000/registro/)
    if request.user.is_authenticated: #r Comprobar si el usuario esta autenticado
        return redirect('inicio')
    else:
        #an BBB-CREAR UN OBJETO PARA GUARGAR EL FORMULARIO EN BASE EL MODELO "User" PARA AUTENTICACION
        register_form = RegisterForm()

        #an GUARDAR USUARIO QUE LLEGUE POR EL FORMULARIO
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Te has registrado correctamente')

                return redirect('/inicio')

        return render(request, 'users/register.html',{
            'title':'Registro',
            'register_form':register_form
        })

#m METODO PARA LOGUEARSE

def login_page(request):

    #R NO MOSTRAR EL ENLACE DE "Login" CUANDO YA SE ESTA REGISTRADO (O YA NO SE PUEDA INGRESAR POR LA URL CUANDO SE PONGUE ASI: http://127.0.0.1:8000/login/)
    if request.user.is_authenticated: #r Comprobar si el usuario esta autenticado
        return redirect('inicio')   
    else:    
        #an CCC-REALIZAR LA AUTENTICACION
        if request.method == 'POST':
            username = request.POST.get('username') #an Recoger el 'username' que llega por la URL
            password = request.POST.get('password') #an Recoger el 'password' que llega por la URL

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)

                return redirect('/inicio')

            else:
                messages.warning(request, 'No te has identificado correctamente')
        
        return render(request, 'users/login.html',{
            'title':'Acceso'
        })

#m METODO PARA CERRAR SECION
def logout_user(request):
    logout(request) #an Django sabe a que usuario desloguear

    return redirect('login')