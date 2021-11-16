# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

class Duck:

    def walk(self):
        print("This duck is walking")
    
    def talk(self):
        print("This duck is qwuacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person:
    
    def catch(self,prey):
        prey.walk()
        prey.talk()
        print("You caught the critter")

duck_1 = Duck()
chicken_1 = Chicken()
person_1 = Person()

person_1.catch(chicken_1)