"""Análisis de Datos de Ventas con Python y Statistics"""
# En este ejemplo, utilizaremos la librería statistics para realizar un análisis básico de datos de ventas.
# Importar la librería statistics

import statistics
# Importar la librería csv para leer archivos CSV
import csv

# Leer los datos de ventas mensuales desde un archivo CSV

monthly_sales = {}
with open('./src/monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
#print(sales)

#Hallar la media
# La media es la suma de todos los valores dividida por el número de valores.
# En este caso, la media nos dará el promedio de ventas mensuales.
mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

#Hallar la mediana
# La mediana es el valor que se encuentra en el medio de un conjunto de datos ordenados.
# Si hay un número par de valores, la mediana es el promedio de los dos valores centrales.
# En este caso, la mediana nos dará una idea de las ventas mensuales típicas.
median_sales = statistics.median(sales)
print(f"La mediana es: {median_sales}")

#Hallar la moda
# La moda es el valor que aparece con más frecuencia en un conjunto de datos.
# En este caso, la moda nos dará el mes con las ventas más comunes.
# Si hay más de un valor que aparece con la misma frecuencia, se devolverá el primero encontrado.
# Si no hay valores repetidos, se devolverá un error.
mode_sales = statistics.mode(sales)
print(f"La moda es: {mode_sales}")

#Desviación Estándar
# La desviación estándar mide la cantidad de variación o dispersión de un conjunto de datos.
# Una desviación estándar baja indica que los datos tienden a estar cerca de la media,
# mientras que una desviación estándar alta indica que los datos están más dispersos.
# En este caso, la desviación estándar nos dará una idea de la variabilidad de las ventas mensuales.
stdev_sales = statistics.stdev(sales)
print(f"La desviación estándar es: {stdev_sales}")

#Hallar la varianza
# La varianza es el promedio de las diferencias al cuadrado respecto a la media.
# En este caso, la varianza nos dará una idea de la variabilidad de las ventas mensuales.
# La varianza es la desviación estándar al cuadrado.
# La varianza es útil para entender la dispersión de los datos.
variance_sales = statistics.variance(sales)
print(f"La varianza es: {variance_sales}")

max_sales = max(sales)
min_sales = min(sales)

#Hallar el rango
# El rango es la diferencia entre el valor máximo y el valor mínimo en un conjunto de datos.
# En este caso, el rango nos dará una idea de la amplitud de las ventas mensuales.
range_sales = max_sales - min_sales
print(f'Rango de ventas: {range_sales}')