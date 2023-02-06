from tkinter import *

ventana = Tk()
ventana.geometry("600x600")

mi_menu = Menu(ventana) #1 Crear un menu dentro de la ventana principal
ventana.config(menu=mi_menu) #1 Indicarle que vas a cargar un menú

archivo = Menu(mi_menu, tearoff=0) #1 Crear un menu y que este vinculado a la variable mi_menu / tearoff = 0 sirve para quitar el separador al inicio
archivo.add_command(label="Nuevo archivo")
archivo.add_command(label="Nuevo ventana")
archivo.add_separator() #1 Crear un separador o -----------------
archivo.add_command(label="Abrir archivo")
archivo.add_command(label="Abrir carpeta")
archivo.add_separator()
archivo.add_command(label="Salir", command=ventana.quit) #1 ventana.quit sirve para cerrar la ventana

mi_menu.add_cascade(label="Archivo", menu=archivo) #1 Añadir un menu desplegable(add_cascade) y vincular con "archivo"
mi_menu.add_command(label="Editar") #1 Añadir un elemento(add_command)
mi_menu.add_command(label="Selección") #1 Añadir un elemento(add_command)

ventana.mainloop()