"""Ejercicio de clase 26"""

#Leer todas las líneas en una lista
with open('./src/cuento.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines() #Lee todas las líneas y las guarda en una lista
    print(len(lines))