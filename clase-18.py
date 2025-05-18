"""Funciones Lambda en Python: Uso y Aplicaciones Prácticas"""
# En este ejercicio, se explorará el uso de funciones lambda en Python y se presentarán algunas aplicaciones prácticas.
# Las funciones lambda son funciones anónimas que se pueden definir en una sola línea y son útiles para operaciones simples.

# Ejemplo de una función lambda para sumar dos números
suma = lambda a, b: a + b
print("Resultado de la suma:", suma(5, 3))

# Ejemplo de una función lambda para multiplicar dos números
multiplicacion = lambda a, b: a * b
print("Resultado de la multiplicación:", multiplicacion(5, 3))

# Uso de funciones lambda con la función map
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print("Cuadrados:", cuadrados)

# Uso de funciones lambda con la función filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)
# Uso de funciones lambda con la función reduce
from functools import reduce
numeros = [1, 2, 3, 4, 5]
suma_total = reduce(lambda x, y: x + y, numeros)
print("Suma total:", suma_total)
# Uso de funciones lambda para ordenar una lista de tuplas
personas = [("Juan", 25), ("Ana", 30), ("Pedro", 20)]
personas_ordenadas = sorted(personas, key=lambda x: x[1])
print("Personas ordenadas por edad:", personas_ordenadas)

# Uso de funciones lambda para crear una función de multiplicación
multiplicador = lambda x: lambda y: x * y
doble = multiplicador(2)
print("Doble de 5:", doble(5))

personas = [
    ("Juan", 25, 175),
    ("Ana", 30, 160),
    ("Pedro", 20, 180),
    ("Luisa", 30, 170),
    ("Mario", 25, 165)
]

# Ordenar por edad y altura
personas_ordenadas = sorted(personas, key=lambda x: (x[1], x[2]))
print("Personas ordenadas por edad y altura:", personas_ordenadas)