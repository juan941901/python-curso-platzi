"""Manejo de Archivos JSON en Python para Aplicaciones Web y APIs"""
import csv
import json

#Lectura del archivo
with open('./src/products.json', mode='r') as file:
    products = json.load(file)

with open('./src/products_json.csv', mode='w', newline='') as updated_file:
    csv_writer = csv.DictWriter(updated_file, fieldnames=list(products[0].keys()))
    csv_writer.writeheader()

    for row in products:
        csv_writer.writerow(row)

#Lectura del archivo CSV
with open('./src/products_json.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    data = list(csv_reader)

    # Escribir el archivo json
with open('./src/products_json.json', mode='w') as file_new_json:
    json.dump(data, file_new_json, indent=4)
