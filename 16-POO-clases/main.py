# PROGRAMACION ORIENTADA A OBJETOS (POO o OOP)

# DEFINIR UNA CLASE (MOLDE PARA CREAR MAS OBJETOS DE ESE TIPO
# (COCHE) CON CARACTERISTICAS SIMILARES)

class Coche:

    # ATRIBUTOS O PROPIEDADES (ANTES ERA VARIABLES)
    # CARACTERISTICAS DEL COCHE
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # METODOS, SON ACCIONES QUE HACE EL BOJETO (COCHE) (ANTES ERA FUNCIONES)
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
    
# FIN DEFINICION CLASE

# CREAR OBJETOS / INSTANCIAR LA CLASE
coche = Coche()

print("COCHE 1")

coche.setColor("amarillo")
coche.setModelo("murcielago")

print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad nueva: ", coche.getVelocidad())

print("__________________________________")

# CREAR MAS OBJETOS
coche2 = Coche()

coche2.setColor("Verde")
coche2.setModelo("Gallardo")

print("COCHE 2")
print(coche2.marca, coche2.getModelo(), coche2.getColor())

print(type(coche2))
