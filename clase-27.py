"""Manipulación de archivos CSV con Python: lectura y escritura"""
# Importar el módulo csv
# Usamos el módulo csv para leer y escribir archivos CSV en Python.
# El módulo csv proporciona funciones y clases para leer y escribir datos en formato CSV (Comma Separated Values).
# CSV es un formato de archivo comúnmente utilizado para almacenar datos tabulares, donde cada línea representa una fila y los valores están separados por comas.
# En este ejemplo, leeremos un archivo CSV llamado "products.csv" que contiene información sobre productos, incluyendo su nombre, precio y cantidad.
# Luego, calcularemos el valor total de cada producto multiplicando el precio por la cantidad y lo agregaremos como una nueva columna llamada "total_value".
# También agregaremos dos nuevas columnas: "nuevo_valor" y "total_value_nuevo", que representan el valor total con un aumento del 10% y del 20%, respectivamente.

import csv

file_path = './src/products.csv'
updated_file_path = './src/products_updated.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    #El DictReader lee el archivo CSV y lo convierte en un diccionario, donde cada fila se representa como un diccionario con los nombres de las columnas como claves.
    #Obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames
    #Agregar nuevas columnas al final de la lista de nombres de columnas
    fieldnames.append('total_value')
    fieldnames.append('nuevo_valor')
    fieldnames.append('total_value_nuevo')

    #Abrir un nuevo archivo CSV para escribir los datos actualizados
    #El modo 'w' indica que estamos abriendo el archivo para escritura. Si el archivo ya existe, se sobrescribirá.
    #Si el archivo no existe, se creará uno nuevo.
    with open(updated_file_path, mode='w', newline='') as updated_file:
        #Crear un objeto DictWriter para escribir en el nuevo archivo CSV
        #El DictWriter toma el archivo de salida y los nombres de las columnas como argumentos.
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        #Escribir los encabezados en el nuevo archivo CSV
        csv_writer.writeheader() #Escribir los encabezados

        #Iterar sobre cada fila del archivo CSV original
        for row in csv_reader:
            print(row)
            #Calcular el valor total multiplicando el precio por la cantidad
            row['total_value'] = float(row['price']) * int(row['quantity'])
            row['nuevo_valor'] = float(row['price']) * int(row['quantity']) * 1.1
            row['total_value_nuevo'] = float(row['price']) * int(row['quantity']) * 1.2
            #Escribir la fila actualizada en el nuevo archivo CSV
            csv_writer.writerow(row)