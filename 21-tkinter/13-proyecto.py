"""
Crear un programa:
(HECHO) - Ventana 
(HECHO) - Tamaño fijo
(HECHO) - No redimensionable
(HECHO) - Un menu (Inicio, Añadir, Información, Salir)
(HECHO) - Opción de salir
(HECHO) - Diferentes pantallas
(HECHO) - Formulario de añadir productos
(HECHO) - Guardar datos temporalmente
(HECHO) - Mostrar datos listados en la pantalla home
"""

from tkinter import *
from tkinter import ttk #r Sirve para organizar mejor visualmente la pantalla con una tabla

#az Definir ventana
ventana = Tk() #r Crear el objeto
"""ventana.geometry("410x350")"""  #r Tamaño de la ventana
ventana.title("Proyecto Tkinter - MIDEZA") #r Titulo
ventana.minsize(410,395) #r Tamaño mínimo de la ventana, se ajusta a la cantidad de contenido de la ventana
ventana.resizable(0,0) #r Ventana no redimencionable

#az Pantallas:
def home(): #r Aqui se definirá las diferentes cosas y "labels" que tendra la pantalla home
    
    #az Montar pantalla
    home_label.config(
        fg="white", #r Color de la letra
        bg="black", #r Fondo de la letra
        font=("Arial", 30), #r Tipo de fuente de la letra y numero de fuente
        padx=160, #r Margenes con respecto al "text" en el eje x
        pady=20 #r Margenes con respecto al "text" en el eje y
    )
    home_label.grid(row=0, column=0)
    
    productos_box.grid(row=2)

    #az Listar productos
    """
    for producto in productos:
        if len(producto) == 3:
            producto.append("AÑADIDO") #r ARTIFICIO = Cuando entra el producto tiene 3 CAMPOS, para que ya no entre a la proxima el mismo producto se le agrega un elemento("AÑADIDO")
            Label(productos_box, text=producto[0]).grid() #r producto[0] mostrará "name_data"
            Label(productos_box, text=producto[1]).grid() #r producto[1] mostrará "precio_data"
            Label(productos_box, text=producto[2]).grid() #r producto[2] mostrará "add_descripcion_entry"
            Label(productos_box, text="*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*").grid() #r linea separadora
    """

    for producto in productos:
        if len(producto) == 3:
            producto.append("AÑADIDO") #r ARTIFICIO = Cuando entra el producto tiene 3 CAMPOS, para que ya no entre a la proxima el mismo producto se le agrega un elemento("AÑADIDO")
            productos_box.insert("", 0, text=producto[0], values=(producto[1])) #r insertar una nueva fila para la tabla

    #az Ocultar otras pantallas (QUE NO SEA LA MISMA PANTALLA DENTRO DE LA FUNCION)
    add_label.grid_remove() #r grid_remove() sirve para quitar la pantalla de otras pantallas
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

def add():
    
    #az Montar pantalla
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=65,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)

    #az Campos del formulario
    add_frame.grid(row=1)

    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_precio_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_precio_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_descripcion_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    add_descripcion_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)  
    add_descripcion_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )
    
    add_separacion.grid(row=4)

    boton.grid(row=5, column=1, sticky=N)
    boton.config(
        padx=15,
        pady=5, 
        bg="green",
        fg="white"
    )

    #az Ocultar otras pantallas
    home_label.grid_remove()
    productos_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

def info():
    
    #az Montar pantalla
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=105,
        pady=20
    )
    info_label.grid(row=0, column=0)

    data_label.grid(row=1, column=0)

    #az Ocultar otras pantallas
    home_label.grid_remove()
    productos_box.grid_remove()
    add_frame.grid_remove()
    add_label.grid_remove()

def add_productos():
    productos.append([
        name_data.get(),
        precio_data.get(),
        add_descripcion_entry.get("1.0", "end-1c") #r Como es un campo de texto(add_descripcion_entry) tiene que llevar parametros especiales ("1.0", "end-1c")
    ])

    name_data.set("") #r Borrar el contenido del campo y colocar un espacion vacio ("")
    precio_data.set("") #r Borrar el contenido del campo y colocar un espacion vacio ("")
    add_descripcion_entry.delete("1.0", END) #r El campo "Text" tiene metodos mas específicos para borrar el campo .delete("1.0", END) 

    home()

#az Variables importantes
productos = []
name_data = StringVar()
precio_data = StringVar()

#az Definir campo de pantalla (HOME) 
home_label = Label(ventana, text="Inicio") #r Era una VARIABLE LOCAL, se tuvo que convertir a una VARIABLE GLOBAL(sacar afuera de la def) para que no salgue error 
productos_box = Frame(ventana, width=250)

Label(ventana).grid(row=1) #r Separador entre la palabra "Inicio" y la TABLA creada

#an Crear tabla para mostrar Producto y Precio
productos_box = ttk.Treeview(height=12, column=2) #r ".Treeview" es para crear la tabla - (height=12) es para el numero de filas que tendra la tabla 
productos_box.grid(row=1, column=0, columnspan=2)
productos_box.heading("#0", text="Producto", anchor=W) #r ".heading" sirve para crear una columna 
productos_box.heading("#1", text="Precio", anchor=W)

#az Definir campo de pantalla (ADD)
add_label = Label(ventana, text="Añadir producto") #r Era una VARIABLE LOCAL, se tuvo que convertir a una VARIABLE GLOBAL(sacar afuera de la def) para que no salgue error

#az Campos del formulario (ADD)
add_frame = Frame(ventana) #r Se crea el Frame para meter hay los Entry y Label para luego ocultarlos en cada función y ya no aparesca el contenido en cada pestaña

add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_precio_label = Label(add_frame, text="Precio: ")
add_precio_entry = Entry(add_frame, textvariable=precio_data)

add_descripcion_label = Label(add_frame, text="Descripción: ")
add_descripcion_entry = Text(add_frame)

add_separacion = Label(add_frame)

boton = Button(add_frame, text="Guardar", command=add_productos) #r Vincular el boton con la función add_productos

#az Definir campo de pantalla (INFO)
info_label = Label(ventana, text="Información") #r Era una VARIABLE LOCAL, se tuvo que convertir a una VARIABLE GLOBAL(sacar afuera de la def) para que no salgue error
data_label = Label(ventana, text="Creado por © 2022, MIDEZA") #r Era una VARIABLE LOCAL, se tuvo que convertir a una VARIABLE GLOBAL(sacar afuera de la def) para que no salgue error

#az Cargar pantalla inicio
home() #r para que cargue automaticamente en la primera pantalla la pantalla de home

#az Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit) #r ventana.quit sirve para salir de la ventana

#az Cargar menú
ventana.config(menu=menu_superior)

#az Cargar ventana
ventana.mainloop()