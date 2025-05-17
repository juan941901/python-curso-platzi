"""Estructuras Condicionales en Programación: Uso de If, Else y Elif"""
# Las estructuras condicionales son fundamentales en la programación, ya que permiten tomar decisiones basadas en condiciones específicas.
# En Python, las estructuras condicionales se implementan utilizando las palabras clave if, else y elif.
# La estructura básica de una sentencia if es la siguiente:
# if condición:
#     # Código a ejecutar si la condición es verdadera
# else:
#     # Código a ejecutar si la condición es falsa
#
# La sentencia if evalúa la condición y, si es verdadera, ejecuta el bloque de código correspondiente. Si la condición es falsa, se ejecuta el bloque de código dentro del else.    
#
# La sentencia elif (else if) se utiliza para evaluar múltiples condiciones. La estructura básica es la siguiente:  
# if condición1:
#     # Código a ejecutar si la condición1 es verdadera
# elif condición2:
#     # Código a ejecutar si la condición2 es verdadera
# elif condición3:
#     # Código a ejecutar si la condición3 es verdadera
# else:
#     # Código a ejecutar si ninguna de las condiciones anteriores es verdadera

x = 10
y = 20

if x > y:
    print("x es mayor que y")
elif x < y:
    print("x es menor que y")
else:
    print("x es igual a y")
# En este ejemplo, se comparan las variables x e y. Si x es mayor que y, se imprime "x es mayor que y". Si x es menor que y, se imprime "x es menor que y". Si ninguna de las condiciones anteriores es verdadera, se imprime "x es igual a y".

if x > 0 and y > 0:
    print("Ambos números son positivos")
elif x < 0 and y < 0:
    print("Ambos números son negativos")
else:
    print("Uno de los números es positivo y el otro es negativo")
# En este ejemplo, se evalúan dos condiciones utilizando el operador lógico and. Si ambas condiciones son verdaderas, se imprime "Ambos números son positivos". Si ambas condiciones son falsas, se imprime "Ambos números son negativos". Si una de las condiciones es verdadera y la otra es falsa, se imprime "Uno de los números es positivo y el otro es negativo".

if x > 0 or y > 0:
    print("Al menos uno de los números es positivo")
elif x < 0 or y < 0:
    print("Al menos uno de los números es negativo")
else:
    print("Ambos números son cero")
# En este ejemplo, se evalúan dos condiciones utilizando el operador lógico or. Si al menos una de las condiciones es verdadera, se imprime "Al menos uno de los números es positivo". Si ambas condiciones son falsas, se imprime "Ambos números son cero".

if not x > y:
    print("x no es mayor que y")
elif not x < y:
    print("x no es menor que y")
else:
    print("x es igual a y")

# En este ejemplo, se utiliza el operador lógico not para invertir el resultado de la comparación. Si x no es mayor que y, se imprime "x no es mayor que y". Si x no es menor que y, se imprime "x no es menor que y". Si ninguna de las condiciones anteriores es verdadera, se imprime "x es igual a y".
# Las estructuras condicionales también pueden anidarse, lo que significa que se pueden incluir sentencias if dentro de otras sentencias if. Esto permite crear flujos de control más complejos y tomar decisiones basadas en múltiples condiciones.
# Ejemplo de anidamiento de estructuras condicionales
if x > 0:
    print("x es positivo")
    if y > 0:
        print("y es positivo")
    else:
        print("y es negativo o cero")

# En resumen, las estructuras condicionales son herramientas poderosas que permiten tomar decisiones en función de condiciones específicas. La combinación de if, else y elif permite crear flujos de control complejos en los programas, lo que facilita la implementación de lógica condicional.
