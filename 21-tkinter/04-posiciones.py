from sqlite3 import TimestampFromTicks
from tkinter import *

ventana = Tk()
#ventana.geometry("700x500") #3 tamaño de la ventana

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white", #3 color de letra
    bg="black", #3 fondo del texto
    padx=50,    #3 ampliar margen del costado izquiero y derecho del texto
    pady=20,    #3 ampliar margen de la parte superior e inferior del texto
    font=("Consolas",30) #3 tipo de fuente y el numero de letra
)
texto.pack(side=TOP) #3 EL pack sirve para GUARDAR LAS MODIFICACIONES HECHAS EN EL TEXTO
                     #4 side sirve para posicionar el texto
texto = Label(ventana, text="Soy MIDEZA")
texto.config(
    #width=400, #3 tamaño del ancho
    height=3,  #3 tamaño de la altura
    bg="orange",
    font=("arial",18),
    padx=10,
    pady=10,
    cursor="spider" #3 forma del cursor
)
texto.pack(side=TOP, fill=X, expand=YES) #4 fill sirve para rellenar en X, y el expand para expandir la caja

texto = Label(ventana, text="Básico 1")
texto.config(
    #width=400, 
    height=3, 
    bg="red",
    font=("arial",18),
    padx=10,
    pady=10,
    cursor="spider" 
)
texto.pack(side=LEFT, fill=X, expand=YES) 

texto = Label(ventana, text="Básico 2")
texto.config(
    #width=400, 
    height=3, 
    bg="green",
    font=("arial",18),
    padx=10,
    pady=10,
    cursor="spider" 
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Básico 3")
texto.config(
    #width=400, 
    height=3, 
    bg="pink",
    font=("arial",18),
    padx=10,
    pady=10,
    cursor="spider" 
)
texto.pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop() #3 para que la ventana se crea y se cargue y funcione hasta que la ventana se cierra