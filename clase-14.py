"""Iteración y control de flujo con bucles en Python"""
# En Python, los bucles se utilizan para repetir un bloque de código varias veces. Los bucles más comunes son el bucle for y el bucle while. A continuación, se presentan ejemplos de ambos tipos de bucles y su uso en Python.
#
# Bucle for
# El bucle for se utiliza para iterar sobre una secuencia (como una lista, una tupla o un rango) y ejecutar un bloque de código para cada elemento de la secuencia. La sintaxis básica del bucle for es la siguiente:
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
# # En este ejemplo, el bucle for itera sobre la lista numbers y imprime cada número en la lista.

for i in range(10):
    print(i)
# # En este ejemplo, el bucle for itera sobre un rango de números del 0 al 9 (10 no incluido) e imprime cada número en el rango.

for i in range(1, 11):
    print(i)
# # En este ejemplo, el bucle for itera sobre un rango de números del 1 al 10 (11 no incluido) e imprime cada número en el rango.

fruits = ["manzana", "banana", "cereza"]
for fruit in fruits:
    print(fruit)
# # En este ejemplo, el bucle for itera sobre la lista fruits y imprime cada fruta en la lista.

for fruit in fruits:
    if fruit == "banana":
        print("¡Encontré una banana!")
    else:
        print(f"Esta fruta no es una banana: {fruit}")
# # En este ejemplo, el bucle for itera sobre la lista fruits y verifica si la fruta actual es una banana. Si es así, imprime un mensaje especial; de lo contrario, imprime un mensaje diferente.

x = 0
# # Bucle while
while x < 10:
    print(x)
    x += 1
# # En este ejemplo, el bucle while continúa ejecutándose mientras x sea menor que 10. En cada iteración, se imprime el valor de x y se incrementa en 1.
# # Cuando x alcanza 10, el bucle se detiene.
# # El bucle while se utiliza cuando no se conoce de antemano cuántas veces se debe ejecutar el bucle. Se basa en una condición que se evalúa en cada iteración.

# # Ejemplo de bucle while con una condición de salida
x = 0
while True:
    print(x)
    x += 1
    if x >= 10:
        break
# # En este ejemplo, el bucle while se ejecuta indefinidamente (True) hasta que se cumple la condición de salida (x >= 10). Cuando se cumple la condición, se utiliza la instrucción break para salir del bucle.

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        continue
    print(number)
# # En este ejemplo, el bucle for itera sobre la lista numbers y, si el número actual es 3, se utiliza la instrucción continue para omitir esa iteración y continuar con la siguiente. Por lo tanto, no se imprimirá el número 3.