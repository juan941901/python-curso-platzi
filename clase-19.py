"""Recursividad en Python: Factoriales y Serie de Fibonacci"""
# En este ejercicio, se explorará el concepto de recursividad en Python y se implementarán funciones recursivas para calcular el factorial de un número y la serie de Fibonacci.
# La recursividad es una técnica de programación en la que una función se llama a sí misma para resolver un problema.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ejemplo de uso
print("Factorial de 5:", factorial(5))
print("Serie de Fibonacci hasta 5:")
for i in range(6):
    print(fibonacci(i), end=" ")

# Ejemplo de uso de recursividad para calcular la suma de una lista
def suma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
print("\nSuma de la lista:", suma_lista(numeros))