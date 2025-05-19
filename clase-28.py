"""Manejo de Archivos JSON en Python para Aplicaciones Web y APIs"""
# El formato JSON (JavaScript Object Notation) es un formato ligero de intercambio de datos que es fácil de leer y escribir para los humanos y fácil de analizar
# y generar para las máquinas.
# JSON es ampliamente utilizado en aplicaciones web y APIs para transmitir datos entre el cliente y el servidor.
# En este ejemplo, leeremos un archivo JSON llamado "products.json" que contiene información sobre productos, incluyendo su nombre, precio y cantidad.
# Luego, calcularemos el valor total de cada producto multiplicando el precio por la cantidad y lo agregaremos como una nueva clave llamada "total_value".

import json

#Lectura del archivo
# with open('./src/products.json', mode='r') as file:
#     products = json.load(file)

# #Mostrar el contenido
# for product in products:
#     #print(product)
#     print(f"Product: {product['name']}, Price: {product['price']}")

# file_path = './src/products.json'

# new_product = {
#     "name": "Wireless Charger",
#     "price": 75,
#     "quantity": 100,
#     "brand": "ChargeMaster",
#     "category": "Accessories",
#     "entry_date": "2024-07-01"
# }

# with open(file_path, mode='r') as file:
#     products = json.load(file)

# products.append(new_product)

# with open(file_path, mode='w') as file:
#     json.dump(products, file, indent=4)

with open('./src/products.json', mode='r') as file:
    products = json.load(file)
    #Mostrar el contenido
    print(list(products[0].keys()))
    print(list(products[0].values()))