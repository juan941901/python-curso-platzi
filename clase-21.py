"""Programación Orientada a Objetos en Python: Clases y Métodos básicos"""
# Definición de la clase
class Persona:
    # Atributos de clase
    especie = "Homo Sapiens"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Métodos de instancia
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños {self.nombre}! Ahora tienes {self.edad} años.")

# Ejemplo de uso
persona1 = Persona("Juan", 30)
persona1.saludar()
persona1.cumplir_anios()

# la variable especie es general para todas las personas, mientras que nombre y edad son por cada objeto instanciado
# para declarar una variable privada, se utiliza un guion bajo al inicio del nombre de la variable _nombre, y para declararla protegida se utiliza un guion bajo doble __nombre
# Si no se coloca ningún guion bajo, la variable es pública y puede ser accedida desde fuera de la clase.
# Las variables privadas no pueden ser accedidas directamente desde fuera de la clase, pero se pueden modificar mediante métodos públicos. y pertenecen unicamente a la clase
# Mientras que las variables protegidas pueden ser accedidas desde subclases, pero no desde fuera de la clase.
# En Python, no existe el concepto de "modificadores de acceso" como en otros lenguajes de programación (por ejemplo, public, private, protected). Sin embargo, se pueden simular utilizando convenciones de nomenclatura.
