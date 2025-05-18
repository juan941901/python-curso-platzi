"""Herencia y Uso de la Función super() en Python"""
# La herencia es un concepto fundamental en la programación orientada a objetos que permite crear nuevas clases basadas en clases existentes.
# Esto permite reutilizar código y crear jerarquías de clases. En Python, la herencia se implementa utilizando paréntesis después del nombre de
# la clase hija, indicando la clase padre de la que hereda.
#
# En este ejemplo, se define una jerarquía de clases que representa seres vivos, personas y estudiantes. La clase `LivingBeing` es la clase base,
# y las clases `Person` y `Student` heredan de ella.
# La clase `Person` hereda de `LivingBeing` y agrega un atributo `age`. La clase `Student` hereda de `Person` y agrega un atributo `student_id`.
# La función `super()` se utiliza para llamar al constructor de la clase padre, lo que permite inicializar los atributos heredados.
# La función `super()` es especialmente útil en la herencia múltiple, donde una clase puede heredar de múltiples clases padre. Permite acceder a 
# métodos y atributos de la clase padre sin necesidad de referirse directamente a su nombre.
# Cada clase hijo debe llamar al constructor de su clase padre utilizando `super().__init__()`, lo que garantiza que los atributos de la clase padre
# se inicialicen correctamente, y pasando los argumentos necesarios de la clase padre.
class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person(LivingBeing):
    # La clase Person hereda de LivingBeing y agrega un atributo age
    # La función super() se utiliza para llamar al constructor de la clase padre (LivingBeing)
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Student(Person):
    # La clase Student hereda de Person y agrega un atributo student_id
    # La función super() se utiliza para llamar al constructor de la clase padre (Person)
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}")

student = Student("Carlos", 21, "S54321")
student.introduce() 
# Salida esperada:
# Hi, I'm Carlos, 21 years old, and my student ID is S54321