"""Manipulación de Archivos TXT y CSV en Python"""
#Leer un archivo línea por línea
# Modos de apertura de archivos
# 'r' - Leer (Read)
# 'a' - Añadir (Append)
# 'w' - Escribir (Write)
# 'x' - Crear (Create)
# 'b' - Binario (Binary)
# 't' - Texto (Text)
# 'r+' - Leer y Escribir (Read and Write) al final
# 'a+' - Añadir y Leer (Append and Read)
# 'w+' - Escribir y Leer (Write and Read) al principio
# 'x+' - Crear y Leer (Create and Read)

# with open('./src/cuento.txt', 'r', encoding='utf-8') as file:
#     for lineas in file:
#         print(lineas.strip()) #Elimina los espacios en blanco al principio y al final con strip()

#Leer todas las líneas en una lista
# with open('./src/cuento.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines() #Lee todas las líneas y las guarda en una lista
#     print(lines)

#Añadir texto
# with open('./src/cuento.txt', 'a', encoding='utf-8') as file:
#     file.write("\n\nBy:ChatGPT") #Escribe al final del archivo

#Sobreescribir el texto
# with open('./src/cuento.txt', 'w', encoding='utf-8') as file:
#     file.write("\n\nBy:ChatGPT") #Escribe al principio del archivo, eliminando el contenido anterior

#Crear un archivo
with open('./src/cuento2.txt', 'x', encoding='utf-8') as file:
    file.write("Este es un nuevo archivo.")
