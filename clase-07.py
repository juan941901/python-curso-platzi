"""Operaciones matemáticas avanzadas en Python: módulo, potencia y más"""
a = 10
b = 3
suma = a + b # Suma de a y b
print(f"La suma de {a} y {b} es: {suma}")
# Resta
resta = a - b # Resta de a y b
print(f"La resta de {a} y {b} es: {resta}") 
# Multiplicación
multiplicacion = a * b # Multiplicación de a y b
print(f"La multiplicación de {a} y {b} es: {multiplicacion}")
# División
division = a / b # División de a entre b
print(f"La división de {a} entre {b} es: {division}")
# Módulo
modulo = a % b # Resto de la división entre a y b
print(f"El módulo de {a} y {b} es: {modulo}")
# Potencia
potencia = a ** b # a elevado a la potencia de b
print(f"La potencia de {a} elevado a {b} es: {potencia}")
# División entera
division_entera = a // b # División entera entre a y b
print(f"La división entera de {a} entre {b} es: {division_entera}")
# Raíz cuadrada
import math # Importa la librería math para operaciones matemáticas avanzadas
raiz_cuadrada = math.sqrt(a) # Raíz cuadrada de a
print(f"La raíz cuadrada de {a} es: {raiz_cuadrada}")   
# Raíz cúbica
raiz_cubica = a ** (1/3) # Raíz cúbica de a
print(f"La raíz cúbica de {a} es: {raiz_cubica}")
# Raíz cúbica con math
raiz_cubica_math = math.pow(a, 1/3) # Raíz cúbica de a usando math
print(f"La raíz cúbica de {a} usando math es: {raiz_cubica_math}")
# Raíz cúbica con math y redondeo
raiz_cubica_redondeada = round(math.pow(a, 1/3), 2) # Raíz cúbica de a usando math y redondeo a 2 decimales
print(f"La raíz cúbica de {a} usando math y redondeo es: {raiz_cubica_redondeada}") 
