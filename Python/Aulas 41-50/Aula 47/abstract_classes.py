# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You drive the motorcycle")

#vehicle_1 = Vehicle()
car_1 = Car()
motorcycle_1 = Motorcycle()

car_1.go()
motorcycle_1.go()