"""Entrada de información y manejo de tipos de datos en Python"""

nombre = input("Introduce tu nombre: ")
print(f"Hola, {nombre}!")

edad = input("Introduce tu edad: ")
print(f"Tu edad es: {edad}")
# edad = float(input("Introduce tu edad: "))

#casting, conversión de tipos de datos

# float
edad = float(edad)
print(type(edad)) # <class 'float'>
print(f"Tu edad es: {edad}")

# int
edad = int(edad)
print(type(edad)) # <class 'int'>
print(f"Tu edad es: {edad}")

# str
edad = str(edad)
print(type(edad)) # <class 'str'>
print(f"Tu edad es: {edad}")

# bool
edad = bool(edad)
print(type(edad)) # <class 'bool'>
print(f"Tu edad es: {edad}")
