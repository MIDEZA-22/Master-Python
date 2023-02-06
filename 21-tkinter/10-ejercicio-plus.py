"""
CALCULADORA:
- Dos campos de texto
- 4 botones para las operaciones 
- Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

class Calculadora:
    
    def __init__(self, alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas

    def cFloat(self, numero):
        try:
            result = float(numero)
        except:
            result = 0
            messagebox.showerror("Error", "Introduce bien los datos")

        return result

    def sumar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) + self.cFloat(self.numero2.get())) #1 lo que sale del get es un str, por lo que se convierte a un int o float
        self.mostrarResultado()
    
    def restar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) - self.cFloat(self.numero2.get())) #1 lo que sale del get es un str, por lo que se convierte a un int o float
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) * self.cFloat(self.numero2.get())) #1 lo que sale del get es un str, por lo que se convierte a un int o float
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(self.cFloat(self.numero1.get()) / self.cFloat(self.numero2.get())) #1 lo que sale del get es un str, por lo que se convierte a un int o float
        self.mostrarResultado()

    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"El resultado es: {self.resultado.get()}")
        self.numero1.set("") #1 Borrar los valores que hay dentro despues de mostrar el msj
        self.numero2.set("") #1 Borrar los valores que hay dentro despues de mostrar el msj
        
ventana = Tk() 
ventana.title("Ejercicio completo con tkinter | MIDEZA")
ventana.geometry("400x400")
ventana.config(bd=25)

calculadora = Calculadora(messagebox)

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
Entry(marco, textvariable=calculadora.numero1, justify="center").pack()

Label(marco, text="Ingrese el segundo número: ").pack()
Entry(marco, textvariable=calculadora.numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=calculadora.sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=calculadora.restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=calculadora.dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()