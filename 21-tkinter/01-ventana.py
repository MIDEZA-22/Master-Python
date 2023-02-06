#5 Tkinter
#3 Módulo para crear interfaces gráficas de usuario 

from tkinter import *
import os.path

class Programa:

    def __init__(self):
        self.title = "Python con Mijail"
        self.icon = "./images/z.ico"
        self.icon_alt = "./21-tkinter/images/z.ico"
        self.size = "770x470"
        self.resizable = False
    
    def cargar(self):

        #2 Crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana

        #2 Titulo de la ventana
        ventana.title(self.title)

        #2 Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        #2 Icono de la ventana
        ventana.iconbitmap(ruta_icono)

        #2 Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        #2 Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        #2 Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1,1) 
        else:
            ventana.resizable(0,0) #4 Se puede cambiar a 1 en cualquiera de los 0, para solo bloquear la altura o la base
            
    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        #2 Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

#4 Instanciar mi programa
programa = Programa()

programa.cargar()
programa.addTexto("Hola")
programa.addTexto("Mijail")
programa.addTexto("como")
programa.addTexto("esta")
programa.addTexto("?")
programa.mostrar()


