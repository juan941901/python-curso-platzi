"""Manejo de Matrices y Tuplas en Python"""
#matrices
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("La matriz es:")
for fila in matriz:
    print(fila)

# Acceder a un elemento de la matriz
print("El elemento en la fila 1, columna 2 es:", matriz[1][2]) # matriz[1][2] accedemos al elemento en la fila 1, columna 2 de la matriz

# Acceder a una fila de la matriz  
print("La fila 1 es:", matriz[1]) # matriz[1] accedemos a la fila 1 de la matriz
# Acceder a una columna de la matriz
columna = [fila[1] for fila in matriz] # Accedemos a la columna 1 de la matriz
print("La columna 1 es:", columna) # Imprimimos la columna 1 de la matriz
# Transponer la matriz
matriz_transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print("La matriz transpuesta es:")
for fila in matriz_transpuesta:
    print(fila)

# Crear una tupla
# Las tuplas son similares a las listas, pero son inmutables (no se pueden modificar una vez creadas)
# Las tuplas se definen con paréntesis (), tambien se pueden crear tuplas con un solo elemento, pero es necesario agregar una coma al final
# Las tuplas pueden contener diferentes tipos de datos, incluyendo listas, cadenas, enteros, flotantes, booleanos y otros tipos de datos
# Crear una tupla vacía
tupla_vacia = ()
tupla = (1, 2, 3, 4, 5)
print("La tupla es:", tupla) # La tupla es: (1, 2, 3, 4, 5)
print(type(tupla)) # type() devuelve el tipo de dato de la variable
# Acceder a un elemento de la tupla
print("El primer elemento es:", tupla[0])
print("El segundo elemento es:", tupla[1])
print("El tercer elemento es:", tupla[2])
print("El último elemento es:", tupla[-1])
# Crear una tupla con diferentes tipos de datos
tupla_diferente = (1, 2.5, "Hola", True, None, [1, 2, 3])
