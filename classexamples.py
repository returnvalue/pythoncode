# Python is an object-oriented programming language.
# Almost everything in Python is an object with properties and methods.
# A class is like an object constructor or blueprint for creating objects.

# A Vehicle class
class Vehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print('Gas tank is now full.')

    def drive(self):
        print(f'The {self.model} is now driving.')


# Constructing an object
vehicle_object = Vehicle('Honda', 'Ridgeline', 'Truck')

# Accessing attribute values
print(vehicle_object.brand)
# Honda
print(vehicle_object.model)
# Ridgeline
print(vehicle_object.type)
# Truck

# Calling methods
vehicle_object.fuel_up()
# Gas tank is now full.
vehicle_object.drive()
# The Ridgeline is now driving.

# Creating multiple objects
vehicle_object = Vehicle('Honda', 'Ridgeline', 'Truck')
a_subaru = Vehicle('Subaru', 'Forester', 'Crossover')
an_suv = Vehicle('Ford', 'Explorer', 'SUV')

# Modifying an attribute directly
cool_new_vehicle = Vehicle('Honda', 'Ridgeline', 'Truck')
cool_new_vehicle.fuel_level = 7


# Define a method to update an attribute’s value
class Vehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print('Gas tank is now full.')

    def drive(self):
        print(f'The {self.model} is now driving.')

    def update_fuel_level(self, new_level):
        if new_level <= self.gas_tank_size:
            self.fuel_level = new_level
        else:
            print('Exceeded capacity')


# Define a method to increment an attribute’s value
class Vehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    def fuel_up(self):
        self.fuel_level = self.gas_tank_size
        print('Gas tank is now full.')

    def drive(self):
        print(f'The {self.model} is now driving.')

    def update_fuel_level(self, new_level):
        if new_level <= self.gas_tank_size:
            self.fuel_level = new_level
        else:
            print('Exceeded capacity')

    def get_gas(self, amount):
        if (self.fuel_level + amount <= self.gas_tank_size):
            self.fuel_level += amount
            print('Added fuel.')
        else:
            print('The tank wont hold that much.')


# The __init__() method for a child class
class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model, type)
        self.battery_size = 85
        self.charge_level = 0


# Adding new methods to a child class
# class ElectricVehicle(Vehicle):
#     def __init__(self, brand, model, type):
#         super().__init__(brand, model, type)
#         self.battery_size = 85
#         self.charge_level = 0
#
#     def charge(self):
#         self.charge_level = 100
#         print('The vehicle is now charged.')
#
#     def fuel_up(self):
#         print('This vehicle has no fuel tank!')


# Using child and parent methods
electric_vehicle = ElectricVehicle('Tesla', 'Model 3', 'Car')
electric_vehicle.charge()
electric_vehicle.drive()


# Overriding parent methods
# class ElectricVehicle(Vehicle):
#     def __init__(self, brand, model, type):
#         super().__init__(brand, model, type)
#         self.battery_size = 85
#         self.charge_level = 0
#
#     def charge(self):
#         self.charge_level = 100
#         print('The vehicle is now charged.')
#
#     def fuel_up(self):
#         print('This vehicle has no fuel tank!')


# Instances as attributes
class Battery:
    def __init__(self, size=85):
        self.size = size
        self.charge_level = 0

    def get_range(self):
        if self.size == 85:
            return 260
        elif self.size == 100:
            return 315


# Storing an instance of a class in an attribute
# class ElectricVehicle(Vehicle):
#     def __init__(self, brand, model, type):
#         super().__init__(brand, model, type)
#         self.battery = Battery()
#
#     def charge(self):
#         self.battery.charge_level = 100
#
#     print('The vehicle is fully charged.')


# Using The Instance
electric_vehicle = ElectricVehicle('Tesla', 'CyberTruck', 'Truck')
electric_vehicle.charge()
# The vehicle is fully charged.
print(electric_vehicle.battery.get_range())
# 260
electric_vehicle.drive()
# The CyberTruck is now driving.

# Storing classes in a file vehicle.py
# class Vehicle:
#     """Vehicle Class data and methods"""
#
#
# class Battery:
#     """Batter Class data and methods"""
#
#
# class ElectricVehicle(Vehicle):
#     """ElectricVehicle Class data and methods"""

# Importing individual classes from a module vehicle_objects.py
# from vehicle import Vehicle, ElectricVehicle
a_mini = Vehicle('Cooper', 'Mini', 'Car')
a_mini.fuel_up()
a_mini.drive()
a_tesla = ElectricVehicle('Tesla', 'Model 3', 'Car')
a_tesla.charge()
a_tesla.drive()

# Importing an entire module
# import vehicle
a_mini = Vehicle('Cooper', 'Mini', 'Car')
a_mini.fuel_up()
a_mini.drive()
a_tesla = ElectricVehicle('Tesla', 'Model 3', 'Car')
a_tesla.charge()
a_tesla.drive()


# Storing objects in a list
# A collection of rental vehicles
# from vehicle import Vehicle, ElectricVehicle

gas_fleet = []
electric_fleet = []

for _ in range(100):
    a_vehicle = Vehicle('Honda', 'Civic', 'Car')
    gas_fleet.append(a_vehicle)
for _ in range(50):
    evehicle = ElectricVehicle('Nissan', 'Leaf', 'Car')
    electric_fleet.append(evehicle)
for a_vehicle in gas_fleet:
    a_vehicle.fuel_up()
for evehicle in electric_fleet:
    evehicle.charge()
print(f'Gas vehicles: {len(gas_fleet)}')
print(f'Electric vehicles: {len(electric_fleet)}')
