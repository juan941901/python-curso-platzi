"""Programación Orientada a Objetos en Python: Clases y Métodos básicos"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no esta disponible")

    def return_book(self):
        self.available = True
        print(f"El libro {self.title} ha sido devuelto")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} No esta disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} No esta en la lista de prestados")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado")

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def show_available_books(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book. author}")

#Crear los libros
book1 = Book("El principito", "Antoine de Saint-ExupÃ©ry")
book2 = Book("1984", "George Orwell")

#Crear usuario
user1 = User("Carli", "001")

#Crear Biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)

#Mostrar libros
library.show_available_books()

#Realizar prestamo
user1.borrow_book(book1)

#Mostrar libros
library.show_available_books()

#Devolver libro
user1.return_book(book1)

#Mostrar libros
library.show_available_books()

"""
    Este ejemplo muestra una implementación básica de un sistema de biblioteca utilizando clases y métodos en Python, los cuales son todos publicos.
    La clase `Book` representa un libro con atributos como título, autor y disponibilidad. Tiene métodos para prestar y devolver libros.
    La clase `User` representa un usuario con atributos como nombre, ID de usuario y una lista de libros prestados. Tiene métodos para prestar y devolver libros.
    La clase `Library` representa una biblioteca con una lista de libros y usuarios. Tiene métodos para agregar libros, registrar usuarios y mostrar libros disponibles.
    El código crea instancias de libros y usuarios, registra un usuario en la biblioteca, muestra los libros disponibles, realiza un préstamo y una devolución de libro.
    Este ejemplo es una buena introducción a la programación orientada a objetos en Python, mostrando cómo crear clases, instancias y métodos para interactuar con los objetos.
    También se puede extender fácilmente para agregar más funcionalidades, como eliminar libros, buscar libros por autor o título, y llevar un registro de los préstamos realizados.
    Se pueden agregar métodos adicionales a las clases para mejorar la funcionalidad, como buscar libros por autor o título, eliminar libros de la biblioteca, y llevar un registro de los préstamos realizados.
    También se pueden agregar métodos adicionales a las clases para mejorar la funcionalidad, como buscar libros por autor o título, eliminar libros de la biblioteca, y llevar un registro de los préstamos realizados.

    Por eso en borrow_book, como recibe el objeto book, se puede acceder a sus atributos y métodos. declaradas dentro de la clase Book.

"""
