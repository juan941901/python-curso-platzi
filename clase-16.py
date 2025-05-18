"""Listas por comprensión en Python: creación y optimización de listas"""
# Las listas por comprensión son una forma concisa y eficiente de crear listas en Python.
# Permiten generar listas a partir de otras listas o iterables, aplicando una expresión a cada elemento.
# La sintaxis básica de una lista por comprensión es:
# [expresión for elemento in iterable]
# Donde:
# - expresión: es la operación que se aplica a cada elemento del iterable.
# - elemento: es la variable que representa cada elemento del iterable.
# - iterable: es la colección de elementos que se va a recorrer.
#
# A continuación, se presentan ejemplos de cómo crear listas por comprensión en Python.
# Crear una lista de números del 1 al 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Crear una lista de cuadrados de los números del 1 al 10
squared_numbers = [x**2 for x in range(1, 11)]
print(squared_numbers)
# Crear una lista de números pares del 1 al 20

celsius = [0, 10, 20, 34.5]
fahrenheit = [((9/5) * temp + 32) for temp in celsius]
# Imprimir la lista de temperaturas en Fahrenheit
print("fahrenheit", fahrenheit)

#hallar números pares
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("even_numbers", even_numbers)

# para este ejemplo se debe tener encuenta que siempre debe ir primero el for y luego el if

#transponer una lista
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print("matrix", matrix)
# Imprimir la matriz transpuesta
print("transposed", transposed)
