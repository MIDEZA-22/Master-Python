from tkinter import *
from PIL import Image, ImageTk #az importar la biblioteca de pillow

ventana = Tk()
ventana.geometry("700x500")

Label(ventana,text="Hola, soy Mijail¡¡").pack(anchor=W)

imagen = Image.open("./21-tkinter/images/TP_1.jpg") #az ubicar la imagen
render = ImageTk.PhotoImage(imagen) #az renderizar la imagen ubicada

Label(ventana,image=render).pack(anchor=E)

ventana.mainloop()

#r INSTALAR EL MODULO PILLOW POR CONSOLA CMD
#az Pilow sirve para cargar imagenes dentro del programa
#az Pegar el siguiente codigo dentro del CMD: pip install --upgrade Pillow
