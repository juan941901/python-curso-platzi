"""Uso de las librerías OS, Math y Random en Python"""
# La librería os proporciona una forma de interactuar con el sistema operativo, permitiendo realizar operaciones como manipulación de archivos y directorios.
# La librería math proporciona funciones matemáticas avanzadas, como trigonometría, logaritmos y constantes matemáticas.
# La librería random permite generar números aleatorios y realizar selecciones aleatorias en colecciones.

# Ejemplo de uso de la librería os
import os
# Obtener el directorio de trabajo actual
current_directory = os.getcwd()
print(f"Directorio de trabajo actual: {current_directory}")
# Crear un nuevo directorio
new_directory = os.path.join(current_directory, "nuevo_directorio")
os.makedirs(new_directory, exist_ok=True)
print(f"Nuevo directorio creado: {new_directory}")
# Listar archivos en el directorio actual
files = os.listdir(current_directory)
print("Archivos en el directorio actual:")
for file in files:
    print(f" - {file}")

# Ejemplo de uso de la librería math
import math
# Calcular la raíz cuadrada de un número
number = 16
square_root = math.sqrt(number)
print(f"La raíz cuadrada de {number} es: {square_root}")
# Calcular el valor de pi
pi_value = math.pi
print(f"El valor de pi es: {pi_value}")
# Calcular el seno de un ángulo en radianes
angle = math.radians(30)  # Convertir grados a radianes
sine_value = math.sin(angle)
print(f"El seno de 30 grados es: {sine_value}")
# Calcular el logaritmo natural de un número
log_value = math.log(10)
print(f"El logaritmo natural de 10 es: {log_value}")
# Calcular el factorial de un número
factorial_value = math.factorial(5)
print(f"El factorial de 5 es: {factorial_value}")
# Ejemplo de uso de la librería random
import random
# Generar un número aleatorio entre 1 y 10
random_number = random.randint(1, 10)
print(f"Número aleatorio entre 1 y 10: {random_number}")
# Seleccionar un elemento aleatorio de una lista
items = ["manzana", "banana", "naranja", "uva"]
random_item = random.choice(items)
print(f"Elemento aleatorio de la lista: {random_item}")
# Barajar una lista de elementos
deck = ["corazones", "diamantes", "tréboles", "picas"]
random.shuffle(deck)
print(f"Baraja de cartas: {deck}")
# Generar una lista de números aleatorios
random_numbers = random.sample(range(1, 101), 5)
print(f"Números aleatorios: {random_numbers}")
# Generar una lista de números aleatorios únicos
unique_random_numbers = random.sample(range(1, 101), 10)
print(f"Números aleatorios únicos: {unique_random_numbers}")
# Generar una lista de números aleatorios con repetición
random_numbers_with_repetition = [random.randint(1, 10) for _ in range(5)]
print(f"Números aleatorios con repetición: {random_numbers_with_repetition}")
# Generar una lista de números aleatorios con una distribución normal
normal_random_numbers = [random.gauss(0, 1) for _ in range(5)]
print(f"Números aleatorios con distribución normal: {normal_random_numbers}")
# Generar una lista de números aleatorios con una distribución uniforme
uniform_random_numbers = [random.uniform(0, 1) for _ in range(5)]