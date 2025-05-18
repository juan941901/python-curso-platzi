"""Programación Orientada a Objetos: Atributos, Métodos y `super()` en Python"""
"""
Para entender mejor la Programación Orientada a Objetos (POO), es esencial recordar los conceptos básicos de atributos y métodos.

Atributos: Son variables que pertenecen a una clase o a sus objetos. Definen las propiedades de un objeto. Por ejemplo, pensemos en una persona: ¿Qué caracteriza a una persona en general?
Las personas tienen nombre, edad, dirección, etc. En términos de POO, estos serían los atributos de la clase Person.
Métodos: Son funciones definidas dentro de una clase que operan sobre sus objetos. Definen los comportamientos de un objeto. Siguiendo con el ejemplo de una persona, ¿Qué acciones puede
realizar una persona? Puede hablar, caminar, comer, etc. En POO, estas acciones serían métodos de la clase Person.

"""

#Ejemplo Básico de una Clase
class Person:
    def __init__(self, name, age):
        self.name = name  # Atributo
        self.age = age    # Atributo

    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años.")  # Método

# Crear una instancia de la clase Person
persona1 = Person("Ana", 30)
persona1.greet()  # Output: Hola, mi nombre es Ana y tengo 30 años.

"""
    al usar herencia vimos el método init() que es le constructor, el mismo es llamado automáticamente cuando se crea una nueva instancia de una clase y se utiliza para inicializar
    los atributos del objeto.
"""

#Ejemplo de Constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Crear una instancia de Person
person1 = Person("Ana", 30)
print(person1.name)  # Output: Ana
print(person1.age)   # Output: 30

#En este ejemplo, el constructor __init__ inicializa los atributos name y age de la clase Person.
"""
    Uso de super() en Python

    La función super() en Python te permite acceder y llamar a métodos definidos en la superclase desde una subclase. Esto es útil cuando quieres extender o modificar la funcionalidad 
    de los métodos de la superclase sin tener que repetir su implementación completa.
"""

#Ejemplo de Uso de super()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello! I am a person.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hi, I'm {self.name}, and I'm a student with ID: {self.student_id}")

# Crear instancia de Student y llamar a greet
student = Student("Ana", 20, "S12345")
student.greet()  # Output: Hello! I am a person.
                 #         Hi, I'm Ana, and I'm a student with ID: S12345

"""
    En este ejemplo:

    La clase Person define un método greet() que imprime un saludo genérico.
    La clase Student, que es una subclase de Person, utiliza super().__init__(name, age) para llamar al constructor de la superclase Person y luego sobrescribe el método greet()
    para agregar información específica del estudiante.

"""

#Jerarquía de Clases y Constructores
#¿Qué sucede si una clase tiene una clase padre y esa clase padre tiene otra clase padre? En este caso, usamos super() para asegurar que todas las clases padre sean inicializadas correctamente.
#Ejemplo de Jerarquía de Clases

class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}")

# Crear instancia de Student
student = Student("Carlos", 21, "S54321")
student.introduce()  # Output: Hi, I'm Carlos, 21 years old, and my student ID is S54321

#En este ejemplo:
"""
    LivingBeing es la clase base que inicializa el atributo name.
    Person es una subclase de LivingBeing que inicializa name a través de super().__init__(name) y luego inicializa age.
    Student es una subclase de Person que inicializa name y age a través de super().__init__(name, age) y luego inicializa student_id.
"""

#Métodos que Vienen por Defecto en Python
# En Python, todas las clases heredan de la clase base object. Esto significa que todas las clases tienen ciertos métodos por defecto, algunos
# de los cuales pueden ser útiles para personalizar el comportamiento de tus clases.
# Algunos de estos métodos son:
# __str__: Se utiliza para definir cómo se debe representar la instancia de la clase como una cadena. Se llama automáticamente cuando se usa print() en la instancia.
# __repr__: Similar a __str__, pero se utiliza para representar la instancia de la clase de una manera que sea útil para los desarrolladores. Se llama automáticamente en el intérprete.
# __eq__: Se utiliza para comparar dos instancias de la clase. Permite definir cómo se deben comparar los objetos de la clase.
# __lt__, __le__, __gt__, __ge__: Se utilizan para definir los operadores de comparación (<, <=, >, >=) para las instancias de la clase.
# __len__: Se utiliza para definir cómo se debe calcular la longitud de una instancia de la clase. Se llama automáticamente cuando se usa len() en la instancia.
# __getitem__: Se utiliza para definir cómo se debe acceder a los elementos de la instancia de la clase utilizando la notación de corchetes (ejemplo: obj[key]).
# __setitem__: Se utiliza para definir cómo se debe establecer un elemento de la instancia de la clase utilizando la notación de corchetes (ejemplo: obj[key] = value).
# __delitem__: Se utiliza para definir cómo se debe eliminar un elemento de la instancia de la clase utilizando la notación de corchetes (ejemplo: del obj[key]).
# __iter__: Se utiliza para definir cómo se debe iterar sobre la instancia de la clase utilizando un bucle for.
# __next__: Se utiliza para definir el siguiente elemento en la iteración de la instancia de la clase.
# __contains__: Se utiliza para definir cómo se debe verificar si un elemento está contenido en la instancia de la clase utilizando el operador in.
# __call__: Se utiliza para definir cómo se debe llamar a la instancia de la clase como si fuera una función.
# __enter__ y __exit__: Se utilizan para definir el comportamiento de la instancia de la clase al usarla con la declaración with.
# __hash__: Se utiliza para definir cómo se debe calcular el hash de la instancia de la clase. Esto es útil si deseas usar la instancia como clave en un diccionario o en un conjunto.
# __del__: Se utiliza para definir el comportamiento de la instancia de la clase al ser eliminada. Se llama automáticamente cuando el objeto es destruido.
# __new__: Se utiliza para crear una nueva instancia de la clase. Es un método estático que se llama antes de __init__ y se utiliza para crear el objeto en sí.
# __init_subclass__: Se utiliza para definir el comportamiento de la clase al ser heredada por una subclase. Se llama automáticamente cuando se crea una nueva subclase.
# __init_subclass__ es un método especial que se llama automáticamente cuando una clase es heredada por una subclase. Permite personalizar el comportamiento de la clase base al ser heredada.
# Se utiliza para realizar acciones específicas al crear una subclase, como registrar la subclase o modificar su comportamiento.
# __init_subclass__ se define dentro de la clase base y se puede utilizar para realizar tareas como:

#ejemplo de __init__, __str__ y __repr__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} años"

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

# Crear instancias de Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Uso de __str__
print(person1)  # Output: Alice, 30 años

# Uso de __repr__
print(repr(person1))  # Output: Person(name=Alice, age=30)