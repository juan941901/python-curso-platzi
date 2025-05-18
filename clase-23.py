"""Herencia y Polimorfismo en Programación Orientada a Objetos"""

# En este ejemplo, creamos una jerarquía de clases para representar diferentes tipos de vehículos
# utilizando herencia y polimorfismo. La clase base es `Vehicle`, y las clases derivadas son `Car`, `Bike` y `Truck`.
# La clase `Customer` representa a un cliente que puede comprar vehículos, y la clase `Dealership` representa una concesionaria de vehículos.
# La clase `Vehicle` tiene métodos para vender un vehículo, verificar su disponibilidad y obtener su precio.
# La clase `Car`, `Bike` y `Truck` heredan de la clase `Vehicle` y implementan sus propios métodos para iniciar y detener el motor.
# La clase `Customer` tiene métodos para comprar un vehículo y consultar su disponibilidad y precio.
# La clase `Dealership` tiene métodos para agregar vehículos al inventario, registrar clientes y mostrar los vehículos disponibles.
# La encapsulación se utiliza para ocultar los detalles internos de la clase `Vehicle`, como el estado de disponibilidad del vehículo.
# La abstracción se utiliza para definir métodos que deben ser implementados por las subclases, como `start_engine` y `stop_engine`.
# La herencia se utiliza para crear una jerarquía de clases que comparten atributos y métodos comunes, como `brand`, `model` y `price`.
# La sobrecarga de métodos se utiliza para permitir que las subclases implementen sus propias versiones de los métodos `start_engine` y `stop_engine`.
# La relación entre las clases `Customer` y `Vehicle` es una relación de asociación, donde un cliente puede comprar varios vehículos.
# La relación entre las clases `Dealership` y `Vehicle` es una relación de composición, donde una concesionaria tiene un inventario de vehículos.
# La relación entre las clases `Dealership` y `Customer` es una relación de asociación, donde una concesionaria tiene varios clientes.
# La relación entre las clases `Vehicle` y sus subclases `Car`, `Bike` y `Truck` es una relación de herencia, donde las subclases heredan atributos y métodos de la clase base.

class Vehicle:
    def __init__(self, brand, model, price):
        #Encapsulacion
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand}. Ha sido vendido")
        else:
            print(f"El vehiculo {self.brand}. No esta disponible")

    #Abstracción
    def check_available(self):
        return self.is_available
    
    #Abstracción
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

#Herencia
class Car(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} está en marcha"
        else:
            return f"El coche {self.brand} no está¡ disponible"
    
    #Polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} No está¡ disponible"

#Herencia
class Bike(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} está¡ en marcha"
        else:
            return f"La bicicleta {self.brand} no está¡ disponible"

     #Polimorfismo   
    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} No está¡ disponible"

#Herencia
class Truck(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} está¡ en marcha"
        else:
            return f"El camión {self.brand} no está¡ disponible"
    
    #Polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} No está¡ disponible"
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento,{vehicle.brand} no está¡ disponible")

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availablity = "Disponible"
        else:
            availablity = "No disponible"
        print(f"El {vehicle.brand} está¡ {availablity} y cuesta {vehicle.get_price()}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido")

    def show_available_vehicle(self):
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")

"""
    Como no hay constructores en las clases hijas, se utiliza el constructor de la clase padre, para asignar los atributos
    de la clase padre a las clases hijas. En este caso, el constructor de la clase padre es el constructor de la clase Vehicle.
    Siendo ejemplo de herencia y encapsulacion.

    Con el metodo start_engine y stop_engine, se implementa el polimorfismo, ya que cada clase hija tiene su propia implementacion, a pesar de que
    en la clase padre se define como un metodo abstracto.
"""

# Crear instancias de vehículos segun el tipo de vehiculo, aplicando la herencia
car1 = Car("Toyota", "Corolla", 20000) 
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

# Crear una instancia de cliente
customer1 = Customer("Carlos")

#Crear una instancia de concesionaria
dealership = Dealership()

#Añadir vehiculos a la concesionaria
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()

#Cliente consultar un vehiculo
customer1.inquire_vehicle(car1)

#Cliente comprar un vehiculo
customer1.buy_vehicle(car1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()