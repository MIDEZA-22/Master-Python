from textwrap import fill
from tkinter import *
from tkinter import font

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter | MIDEZA")

#2 Texto encabezado
encabezado = Label(ventana, text="Formularios con Tkinter - MIDEZA")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Opem Sans", 18),
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W) #1 sticky SIGNIFICA "PEGALO" Y columnspan es para dividir las columnas

#2 Label para el campo (nombre)
label = Label(ventana, text = "Nombres")
label.grid(row=1, column=0, padx=5, pady=5)

#2 Campo de texto (nombre)
campo_texto = Entry(ventana) #1 Entry sirve para crear un campo de texto
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5) #1 grid sirve para CARGAR LOS ELEMENTOS DENTRO DE LA VENTANA A CAMBIO DEL PACK
campo_texto.config(justify="right", state="normal")

#2 Label para el campo (apellidos)
label = Label(ventana, text = "Apellidos")
label.grid(row=2, column=0, padx=5, pady=5)

#2 Campo de texto (apellidos)
campo_texto = Entry(ventana) #1 Entry sirve para crear un campo de texto
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5) #1 grid sirve para CARGAR LOS ELEMENTOS DENTRO DE LA VENTANA A CAMBIO DEL PACK
campo_texto.config(justify="left", state="normal")

#2 Label para el campo (descripción)
label = Label(ventana, text="Descripción")
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)

#2 Campo de texto GRANDE (descripción)
campo_grande = Text(ventana) #1 Text sirve para crear un campo mas grande que el Entry
campo_grande.grid(row=3, column=1)
campo_grande.config(
    width=30, 
    height=5,
    font=("Arial, 12"),
    padx=15,
    pady=15
)

#2 Boton
Label(ventana).grid(row=4, column=1)

boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(padx=10, pady=10, bg="green", fg="white")

ventana.mainloop()