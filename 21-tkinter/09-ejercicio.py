"""
CALCULADORA:
- Dos campos de texto
- 4 botones para las operaciones 
- Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

ventana = Tk() 
ventana.title("Ejercicio completo con tkinter | MIDEZA")
ventana.geometry("400x400")
ventana.config(bd=25)

def cFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showerror("Error", "Introduce bien los datos")

    return result

def sumar():
        resultado.set(cFloat(numero1.get()) + cFloat(numero2.get())) #1 lo que sale del get es un str, por lo que se convierte a un int o float
        mostrarResultado()
  
def restar():
    resultado.set(cFloat(numero1.get()) - cFloat(numero2.get())) #1 lo que sale del get es un str, por lo que se convierte a un int o float
    mostrarResultado()

def multiplicar():
    resultado.set(cFloat(numero1.get()) * cFloat(numero2.get())) #1 lo que sale del get es un str, por lo que se convierte a un int o float
    mostrarResultado()

def dividir():
    resultado.set(cFloat(numero1.get()) / cFloat(numero2.get())) #1 lo que sale del get es un str, por lo que se convierte a un int o float
    mostrarResultado()

def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado es: {resultado.get()}")
    numero1.set("") #1 Borrar los valores que hay dentro despues de mostrar el msj
    numero2.set("") #1 Borrar los valores que hay dentro despues de mostrar el msj

numero1=StringVar()
numero2=StringVar()
resultado=StringVar()

marco = Frame(ventana, width=400, height=170)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID,
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False) #1 Sirve para no deformar el marco

Label(marco, text="Ingrese el primer número: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Ingrese el segundo número: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()