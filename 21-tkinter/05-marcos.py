from textwrap import fill
from tkinter import *
from tkinter import font

ventana = Tk()
ventana.title("Miijail | MIDEZA")
ventana.geometry("700x700")

marco_padre = Frame(ventana, width=250, height=250) #5 "Frame" sirve para cargar el marco, "width" es el ancho y el "height" es la altura
""""
marco_padre.config(
    bg="lightblue"
)
"""
marco_padre.pack(side=BOTTOM,anchor=S, fill=X, expand=YES)

marco = Frame(marco_padre, width=250, height=250) #5 "Frame" sirve para cargar el marco, "width" es el ancho y el "height" es la altura
marco.config(
    bg="red",
    bd=5,
    relief=SOLID
)
marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)

texto = Label(marco, text="Primer marco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial", 20),
)
texto.pack(anchor=CENTER, fill=Y, expand=YES)

marco = Frame(marco_padre, width=250, height=250) #5 "Frame" sirve para cargar el marco, "width" es el ancho y el "height" es la altura
marco.config(
    bg="green",
    bd=5,
    relief=SOLID
)
marco.pack(side=RIGHT, anchor=SE)

marco_padre = Frame(ventana, width=250, height=250) #5 "Frame" sirve para cargar el marco, "width" es el ancho y el "height" es la altura
"""
marco_padre.config(
    bg="lightblue"
)
"""
marco_padre.pack(side=TOP, anchor=N, fill=X, expand=YES)

marco = Frame(marco_padre, width=250, height=250) #5 "Frame" sirve para cargar el marco, "width" es el ancho y el "height" es la altura
marco.config(
    bg="blue",
    bd=5,
    relief=SOLID
)
marco.pack(side=LEFT)

marco = Frame(marco_padre, width=250, height=250) #5 "Frame" sirve para cargar el marco, "width" es el ancho y el "height" es la altura
marco.config(
    bg="orange",
    bd=5,
    relief=SOLID
)
marco.pack(side=RIGHT)

ventana.mainloop()