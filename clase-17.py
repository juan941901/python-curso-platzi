"""Funciones y Parámetros en Python: Crea una Calculadora Básica"""
# En este ejercicio, se implementará una calculadora básica en Python utilizando funciones y parámetros.
# La calculadora realizará operaciones de suma, resta, multiplicación y división.

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."

# Ejemplo de uso de la calculadora
num1 = 10
num2 = 5

print("Suma:", sumar(num1, num2))
print("Resta:", restar(num1, num2))
print("Multiplicación:", multiplicar(num1, num2))
print("División:", dividir(num1, num2))
# Ejemplo de uso de la calculadora con división por cero
num3 = 10
num4 = 0
print("División:", dividir(num3, num4))