"""Manejo de Cadenas y Operaciones Básicas en Python"""
# Definición de variables

name = 'Juan'

print(type(name))  # Imprime el tipo de la variable name

name = '''Juan
Pérez'''    # El uso de comillas triples permite cadenas multilínea, imprimiendo el valor tal cual como se esta escribiendo

print(name)  # Imprime el valor de la variable name

"""indexación"""
# La indexación permite acceder a caracteres individuales dentro de una cadena
# La indexación en Python comienza desde 0
# La cadena "Juan" tiene los siguientes índices:
# J = 0
# u = 1
# a = 2
# n = 3

print(name[0])  # Imprime el primer carácter de la cadena name
print(name[1])  # Imprime el segundo carácter de la cadena name
print(name[2])  # Imprime el tercer carácter de la cadena name
print(name[3])  # Imprime el cuarto carácter de la cadena name

last_name = 'Pérez'
print(last_name)
print(name + ' ' +last_name)  # Imprime la concatenación de las cadenas name y last_name, se usa el signo + para concatenar

print(name * 5)  # Imprime la cadena name repetida 5 veces

print(len(name))  # Imprime la longitud de la cadena name, es decir, el número de caracteres que contiene, con uso de la función len()

"""Métodos de cadenas"""
# Los métodos de cadenas son funciones que se pueden aplicar a las cadenas para realizar diversas operaciones
#.count() 
#.capitalize()
#.title() 
#.swapcase() 
#.replace(,) 
#.split() 
#.strip() 
#.lstrip() 
#.rstrip() 
#.find()
#.index() 
#eval()	#Este y el siguiente son super métodos
#exec()

print(name.lower())  # Convierte la cadena name a minúsculas
print(name.upper())  # Convierte la cadena name a mayúsculas
print(name.title())  # Convierte la cadena name a formato título (primera letra de cada palabra en mayúscula)
print(name.capitalize())  # Convierte la primera letra de la cadena name a mayúscula
print(name.swapcase())  # Cambia las mayúsculas por minúsculas y viceversa en la cadena name
print(name.replace('a', 'o'))  # Reemplaza todas las ocurrencias de 'a' por 'o' en la cadena name
print(name.split(' '))  # Divide la cadena name en una lista de palabras usando el espacio como separador
print(name.strip())  # Elimina los espacios en blanco al inicio y al final de la cadena name