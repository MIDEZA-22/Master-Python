from tkinter import *
from tokenize import String

ventana = Tk()
ventana.geometry("800x500")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 20)
)
encabezado.grid(row=0, column=0, columnspan=5, sticky=W)

#4 Botones check
def mostrarProfesion():
    texto = ""

    if web.get():
        texto += "Desarrollo web"

    if movil.get():
        if web.get():    
            texto += " / Desarrollo movil"
        else:    
            texto += "Desarrollo web"

    mostrar.config(
        text=texto,
        bg="green",
        fg="white"
    )

web = IntVar()
movil = IntVar()

Label(ventana, text="¿A que te dedicas?").grid(row=1, column=0)
Checkbutton(
    ventana, 
    text="Desarrollo web", 
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0)
Checkbutton(
    ventana,
    text="Desarrollo movil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=3, column=0)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)

#4 Radio buttons
def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()
opcion.set(None) #1 Para que los radios al iniciar el programa no aparescan marcados

Label(ventana, text="¿Cual es tu género?").grid(row=5)

Radiobutton(
    ventana, 
    text="Masculino",
    value="Masculinoss", #1 Lo que se imprimira al hacer click en el radio
    variable=opcion,
    command=marcar
).grid(row=6)

Radiobutton(
    ventana, 
    text="Femenino",
    value="Femeninos", #1 Lo que se imprimira al hacer click en el radio
    variable=opcion,
    command=marcar
).grid(row=7)

marcado = Label(ventana)
marcado.grid(row=8)

#4 Option Menú
def seleccionar():
    seleccionado.config(text=opcion.get())

opcion = StringVar()
opcion.set("Opcion 1") #1 Colocar una opcion por defecto

Label(ventana, text="Selecione una opción").grid(row=5, column=1)

select = OptionMenu(ventana, opcion, "Opcion 1", "Opcion 2", "Opcion 3" )
select.grid(row=6, column=1)

Button(ventana, text="ver", command=seleccionar).grid(row=7, column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=8, column=1)

ventana.mainloop()

