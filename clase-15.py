"""Iteradores y Generadores en Python: Uso Eficiente de Memoria"""
# Los iteradores y generadores son herramientas poderosas en Python que permiten trabajar con secuencias de datos de manera eficiente y flexible.
# Un iterador es un objeto que implementa el protocolo de iteración de Python, que consiste en los métodos __iter__() y __next__(). Los iteradores permiten recorrer elementos de una colección sin necesidad de cargar todos los elementos en memoria al mismo tiempo.
# Un generador, por otro lado, es una función que utiliza la palabra clave yield para devolver valores de forma paulatina, en lugar de devolver todos los valores de una vez. Los generadores son una forma conveniente de crear iteradores.

# A continuación, se presentan ejemplos de cómo crear y utilizar iteradores y generadores en Python.
# Ejemplo de un iterador personalizado

#Crear una lista de números del 1 al 10
numbers = [1, 2, 3, 4]
# Crear un iterador personalizado
myIterator = iter(numbers)
#usar next() para obtener el siguiente elemento del iterador
print(next(myIterator))  # Imprime el primer elemento (1)
print(next(myIterator))  # Imprime el segundo elemento (2)
print(next(myIterator))  # Imprime el tercer elemento (3)
print(next(myIterator))  # Imprime el cuarto elemento (4)
# Intentar obtener el siguiente elemento del iterador después de que se hayan agotado los elementos

#iterar a través de una cadena
text = "hola mundo"
iteratorText = iter(text)

for char in iteratorText:
    print(char)  # Imprime cada carácter de la cadena "hola mundo"

# Iterador para los números impares
limite = 10

odd_numbers = iter(range(1, limite + 1, 2))

for number in odd_numbers:
    print(number)  # Imprime los números impares del 1 al 10

# Iterador para los números pares
limite = 10

odd_numbers = iter(range(0, limite + 1, 2))

for number in odd_numbers:
    print(number)  # Imprime los números impares del 1 al 10

# Generador
def my_generator():
    yield 1
    yield 2
    yield 3

# Crear una instancia del generador
for i in my_generator():
    print(i)  # Imprime 1, luego 2, luego 3

#ejemplo con serie de Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
# Crear una instancia del generador
for num in fibonacci(10):
    print(num)  # Imprime los primeros 10 números de la serie de Fibonacci