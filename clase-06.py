"""Usos del print"""
# El uso de print() es para imprimir en pantalla el resultado de una operación o el valor de una variable

#Uso de la coma en print
#La coma dentro de la función print se usa para separar varios argumentos. Al hacerlo, Python añade automáticamente un espacio entre los argumentos. Esto es diferente a concatenar cadenas con el operador +, que no añade espacios adicionales.
#Ejemplo:
print("Nunca", "pares", "de", "aprender") # Imprime: Nunca pares de aprender

#Por otro lado, al concatenar cadenas con el operador +, los elementos se unen sin ningún espacio adicional, a menos que lo añadas explícitamente
print("Nunca" + "pares" +  "de" +  "aprender") # Imprime: Nuncaparesdeaprender

#Para añadir un espacio explícitamente cuando concatenas cadenas, debes incluirlo dentro de las comillas.
print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender") # Imprime: Nunca pares de aprender

#Uso de la función sep()
#La función sep() se utiliza para especificar el separador entre los argumentos que se pasan a la función print(). Por defecto, el separador es un espacio en blanco. Puedes cambiarlo a cualquier otro carácter o cadena de caracteres.
print("Nunca", "pares", "de", "aprender", sep=",") # Imprime: Nunca,pares,de,aprender

#uso de la función end()
#La función end() se utiliza para especificar qué se imprime al final de la línea. Por defecto, Python añade un salto de línea al final de cada llamada a print(). Puedes cambiarlo a cualquier otra cadena de caracteres.
print("Nunca", "pares", "de", "aprender", end="!") # Imprime: Nunca pares de aprender!

#Impresion de variables
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author) # Imprime: Frase: Nunca pares de aprender Autor: Platzi

# 7. Uso de formato con format
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase: {}, Autor: {}".format(frase, author)) # Imprime: Frase: Nunca pares de aprender, Autor: Platzi

# 8. Impresión con formato específico
# Puedes controlar el formato de los números al imprimir. En este ejemplo, :.2f indica que el número debe mostrarse con dos decimales. Así, imprimirá “Valor: 3.14”, redondeando el número a dos decimales. Esto es especialmente útil cuando trabajas con datos numéricos y necesitas un formato específico.
valor = 3.14159
print("Valor: {:.2f}".format(valor)) # Imprime: Valor: 3.14

# 9. Saltos de línea y caracteres especiales
print("Primera línea\nSegunda línea") # Imprime: Primera línea

# Segunda línea
#Si necesitas imprimir una ruta de archivo en Windows, que incluya barras invertidas, también necesitarás usar secuencias de escape para evitar que Python interprete las barras invertidas como parte de secuencias de escape. Por ejemplo:
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt") # Imprime: La ruta de archivo es: C:\Users\Usuario\Desktop\archivo.txt