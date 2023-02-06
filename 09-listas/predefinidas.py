cantantes = ['2pac', 'Drake', 'Bad Bunny', 'Julio Iglesias']
numeros = [1, 2, 5, 8, 3, 4]

# ORDENAR
#print(numeros)
numeros.sort()
#print(numeros)

# AÑADIR ELEMENTOS
cantantes.append("Natos y Waor")
cantantes.insert(1, "David Bisbal")
#print(cantantes)

# ELIMINAR ELEMENTOS
cantantes.pop(1)
cantantes.remove('Bad Bunny')
#print(cantantes)

# DAR LA VUELTA
print(numeros)
numeros.reverse()
print(numeros)

# BUSCAR DENTRO DE UNA LISTA
print('Drake' in  cantantes)

# CONTAR ELEMENTOS
print(cantantes)
print(len(cantantes))

# CUANTAS VECES APARECE UN ELEMENTO
numeros.append(8)
print(numeros.count(8))

# CONSEGUIR INDICE
print(cantantes.index("Drake"))

# UNIR LISTAS
cantantes.extend(numeros)
print(cantantes)