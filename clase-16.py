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
squared_numbers = [n**2 for n in numbers]
