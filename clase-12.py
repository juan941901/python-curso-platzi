"""Diccionarios en Python: Uso y Manipulación de Datos"""
# Definición de un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

print("Diccionario original:", mi_diccionario)
# Acceso a valores
print("Nombre:", mi_diccionario["nombre"])
print("Edad:", mi_diccionario["edad"])
print("Ciudad:", mi_diccionario["ciudad"])

# Modificación de valores
mi_diccionario["edad"] = 31 
print("Edad modificada:", mi_diccionario["edad"])
# Adición de nuevos pares clave-valor
mi_diccionario["profesión"] = "Ingeniero"
print("Diccionario modificado:", mi_diccionario)
# Eliminación de un par clave-valor
del mi_diccionario["ciudad"]    
print("Diccionario después de eliminar ciudad:", mi_diccionario)
# Verificación de la existencia de una clave
if "nombre" in mi_diccionario:
    print("La clave 'nombre' existe en el diccionario.")

#Metodo de diccionario
# Obtener todas las claves
claves = mi_diccionario.keys()
print("Claves del diccionario:", list(claves))
# Obtener todos los valores
valores = mi_diccionario.values()
print("Valores del diccionario:", list(valores))
# Obtener todos los pares clave-valor
items = mi_diccionario.items()
print("Pares clave-valor del diccionario:", list(items))
# Crear un nuevo diccionario
nuevo_diccionario = dict(nombre="Ana", edad=25, ciudad="Barcelona")
print("Nuevo diccionario:", nuevo_diccionario)
# Unir dos diccionarios
mi_diccionario.update(nuevo_diccionario)
print("Diccionario después de unir:", mi_diccionario)
# Crear un diccionario anidado
diccionario_anidado = {
    "persona": {
        "nombre": "Pedro",
        "edad": 28
    },
    "ciudad": "Valencia"
}
print("Diccionario anidado:", diccionario_anidado)
# Acceder a un valor en un diccionario anidado
print("Nombre de la persona:", diccionario_anidado["persona"]["nombre"])
print("Edad de la persona:", diccionario_anidado["persona"]["edad"])
print("Ciudad:", diccionario_anidado["ciudad"])
# Crear un diccionario con comprensión de diccionarios
diccionario_comprension = {x: x**2 for x in range(5)}
print("Diccionario con comprensión:", diccionario_comprension)