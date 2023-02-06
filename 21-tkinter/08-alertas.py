from tkinter import *
from tkinter import messagebox as MessageBox #1 sirve para ser alertas


ventana =  Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showerror("Alerta", "Soy MIDEZA") #1 Mostrar tipos de errores(showerror, showwarning, etc)

Button(ventana, text="Mostrar alerta¡¡¡", command=sacarAlerta).pack()

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Continuar ejecutando?")
    if resultado != "yes":
        MessageBox.showinfo("Chaoo¡¡", f"Adios {nombre}") #1 Mostrar sair antes de cerrar
        ventana.destroy() #1 Cerrar la ventana

Button(ventana, text="Salir", command=lambda: salir("MIDEZA")).pack() #1 "lambda:" sirve para retener la ejecución de la función salir("MIDEZA"). Si no se usaria lambda: la función se ejecutaria automaticamente. Es decir, ni se ejecute el programa se lanzaria la funcion

ventana.mainloop()