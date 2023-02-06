import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nOK {usuario[1]}. Vamos a crear una nueva nota")
       
        titulo = input("\nIntroduce el título de tu nota: ")
        descripcion = input("Ingrese un contenido: ")
        
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")
        
        else:
            print(f"\nNo se ha guardado al nota, lo siento {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\n{usuario[1]}, Aqui tienes tus notas: ")

        nota = modelo.Nota(usuario[0],"","") #2 La coma se pone cuando llegan los parametros vacios
        notas = nota.listar()

        for nota in notas:
            print("\n*******************************************")
            print(nota[2])
            print(nota[3]) 
            print("*******************************************")

    def borrar(self, usuario):
        print(f"\nOK {usuario[1]}. Vamos a borrar notas")

        titulo = input("\nIntroduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo, "")
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"\nHemos borrado la nota: {nota.titulo}")

        else:
            print("No se ha borrado la nota, prueba luego")