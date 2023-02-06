from tkinter import *

ventana = Tk()
ventana.geometry("700x700")
ventana.config(
    bd=50
)

def getDato():
    resultado.set(dato.get())

    if len(resultado.get()) >= 1:
        texto_recogido.config(
            bg="green",
            g="white"
        )

dato = StringVar() #1 StringVar asigna un valor utilizando un campo de formulario
resultado = StringVar()

Label(ventana, text="Ingrese un texto").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW) #1 textvariable sirve para guardar una variable

Label(ventana, text="Dato recogido: ").pack(anchor=NW)
texto_recogido = Label(ventana, textvariable=resultado)
texto_recogido.pack(anchor=NW)

Button(ventana, text="Mostrar dato", command=getDato).pack(anchor=NW) #1 command sirve para que la funcion actue al hacer click

ventana.mainloop()