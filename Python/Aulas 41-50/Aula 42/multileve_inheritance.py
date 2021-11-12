# multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating.")
    
class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog_1 = Dog()

dog_1.bark()
dog_1.eat()
print(dog_1.alive)