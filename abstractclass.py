# Simple Class With Inheritance
class Vehicle:
    def __init__(self):
        super().__init__()

    def go_forward(self):
        print('Driving forward.')


class Car(Vehicle):
    def __init__(self):
        super().__init__()


class Truck(Vehicle):
    def __init__(self):
        super().__init__()


vehicle1 = Vehicle()

car1 = Car()
car1.go_forward()

truck1 = Truck()
truck1.go_forward()

# Adding Abstract Base Class
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def go_forward(self):
        pass


# Adding A Subclass
class Car(Vehicle):
    def __init__(self, press_accelerator):
        super().__init__()
        self.press_accelerator = press_accelerator

    def go_forward(self):
        if self.press_accelerator:
            print('Driving forward')
        else:
            print('Press the accelerator to drive forward')


car1 = Car(True)
car1.go_forward()


# A Second Subclass
class Truck(Vehicle):
    def __init__(self, press_accelerator):
        super().__init__()
        self.press_accelerator = press_accelerator

    def go_forward(self):
        if self.press_accelerator:
            print('Driving forward')
        else:
            print('Press the accelerator to drive forward')


truck1 = Truck(False)
truck1.go_forward()

truck2 = Truck(True)
truck2.go_forward()
