"""Funciones y Parámetros en Python: Crea una Calculadora Básica"""
# En este ejercicio, se implementará una calculadora básica en Python utilizando funciones y parámetros.
# La calculadora realizará operaciones de suma, resta, multiplicación y división.

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."

# Ejemplo de uso de la calculadora
def calculadora():
    while True:
        print("\n--- Calculadora Básica ---")
        print("Seleccione una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        operacion = input("Ingrese el número de la operación deseada (1/2/3/4/5): ")

        if operacion == '5':
            print("Saliendo de la calculadora.")
            break
        if operacion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if operacion == '1':
                resultado = sumar(num1, num2)
            elif operacion == '2':
                resultado = restar(num1, num2)
            elif operacion == '3':
                resultado = multiplicar(num1, num2)
            elif operacion == '4':
                resultado = dividir(num1, num2)

            print(f"El resultado es: {resultado}")
        else:
            print("Operación no válida.")
# Llamar a la función calculadora para iniciar el programa
calculadora()
# En este ejercicio, se implementará una calculadora básica en Python utilizando funciones y parámetros.