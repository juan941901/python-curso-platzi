"""Manipulación de Listas en Python: Creación, Indexación y Métodos basicos"""

# Crear una lista vacía
todo_list = [ "comprar leche", "estudiar Python", "hacer ejercicio"]
print(todo_list) # ['comprar leche', 'estudiar Python', 'hacer ejercicio']

# Crear una lista con numeros
numeros = [1, 2, 3, 4, "cinco"]
print(numeros) # [1, 2, 3, 4, "cinco"]

# Crear una lista con diferentes tipos de datos
mi_lista = [1, 2.5, "Hola", True, None, [1, 2, 3]]
print(mi_lista) # [1, 2.5, 'Hola', True, None, [1, 2, 3]]

print("La lista tiene", len(mi_lista), "elementos") # La lista tiene 6 elementos, con len contamos los elementos de la lista
print("El primer elemento es:", mi_lista[0]) # Usamos [], con el índice 0 accedemos al primer elemento de la lista
print("El segundo elemento es:", mi_lista[1]) # Usamos [], con el índice 1 accedemos al segundo elemento de la lista    
print("El tercer elemento es:", mi_lista[2]) # Usamos [], con el índice 2 accedemos al tercer elemento de la lista
print("El último elemento es:", mi_lista[-1]) # Usamos [], con el índice -1 accedemos al último elemento de la lista

string = "Hola Mundo"
print("El primer caracter es:", string[0]) # Usamos [], con el índice 0 accedemos al primer caracter de la cadena  
print("El segundo caracter es:", string[1]) # Usamos [], con el índice 1 accedemos al segundo caracter de la cadena
print("El tercer caracter es:", string[2]) # Usamos [], con el índice 2 accedemos al tercer caracter de la cadena
print("El último caracter es:", string[-1]) # Usamos [], con el índice -1 accedemos al último caracter de la cadena

#slice
print("Los primeros 5 elementos son:", mi_lista[:5]) # [:5] accedemos a los primeros 5 elementos de la lista
print("Los últimos 5 elementos son:", mi_lista[-5:]) # [-5:] accedemos a los últimos 5 elementos de la lista    
print("Los elementos del índice 1 al 3 son:", mi_lista[1:4]) # [1:4] accedemos a los elementos del índice 1 al 3 de la lista
print("Los elementos del índice 1 al 3 son:", mi_lista[:]) # [:] accedemos a todos los elementos de la lista

#metodos
print("La lista original es:", mi_lista) # La lista original es: [1, 2.5, 'Hola', True, None, [1, 2, 3]]
mi_lista.append("Nuevo elemento") # append() agrega un nuevo elemento al final de la lista
print("La lista después de append es:", mi_lista) # La lista después de append es: [1, 2.5, 'Hola', True, None, [1, 2, 3], 'Nuevo elemento']
mi_lista.append([1, 2, 3])
mi_lista.insert(0, "Elemento al inicio") # insert() agrega un nuevo elemento en la posición 0 de la lista
print("La lista después de insert es:", mi_lista) # La lista después de insert es: ['Elemento al inicio', 1, 2.5, 'Hola', True, None, [1, 2, 3], 'Nuevo elemento']

print(mi_lista.index("Hola")) # index() devuelve el índice del primer elemento que coincide con el valor dado
print(mi_lista.count(1)) # count() devuelve el número de veces que aparece un elemento en la lista
mi_lista.remove("Elemento al inicio") # remove() elimina el primer elemento que coincide con el valor dado
print("La lista después de remove es:", mi_lista) # La lista después de remove es: [1, 2.5, 'Hola', True, None, [1, 2, 3], 'Nuevo elemento']
mi_lista.pop() # pop() elimina el último elemento de la lista y lo devuelve
print("La lista después de pop es:", mi_lista) # La lista después de pop es: [1, 2.5, 'Hola', True, None, [1, 2, 3]]
mi_lista.pop(0) # pop() elimina el elemento en la posición 0 de la lista y lo devuelve
print("La lista después de pop(0) es:", mi_lista) # La lista después de pop(0) es: [2.5, 'Hola', True, None, [1, 2, 3]]
mi_lista.clear() # clear() elimina todos los elementos de la lista
print("La lista después de clear es:", mi_lista) # La lista después de clear es: []

numeros.pop()
print(max(numeros)) # max() devuelve el elemento máximo de la lista
print(min(numeros)) # min() devuelve el elemento mínimo de la lista

del numeros[0] # del elimina el elemento en la posición 0 de la lista
print("La lista después de del es:", numeros) # La lista después de del es: [2, 3, 4]

#slicing
a = [1, 2, 3, 4, 5]
b = a # b es una referencia a la lista a, y comparte el mismo espacio en memoria
del a[0] # al eliminar el primer elemento de a, también se elimina de b
print("La lista a es:", a) # La lista a es: [2, 3, 4, 5]
print("La lista b es:", b) # La lista b es: [2, 3, 4, 5]
# Para crear una copia de la lista a, usamos slicing
c = a[:] # c es una copia de la lista a, y no comparte el mismo espacio en memoria
a.append(6) # al agregar un nuevo elemento a a, no se afecta a c
print("La lista a es:", a) # La lista a es: [2, 3, 4, 5, 6]
print("La lista b es:", b) # La lista b es: [2, 3, 4, 5, 6]
print("La lista c es:", c) # La lista c es: [2, 3, 4, 5]