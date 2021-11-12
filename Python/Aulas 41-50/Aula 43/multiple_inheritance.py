# -----------------------------------------------------------------------------
# multiple inheritance = when a child class is derived from more than one parent class

class Prey:
    
    def flee(self):
        print("This animal flees")


class Predator:

    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit_1 = Rabbit()
hawk_1 = Hawk()
fish_1 = Fish()

fish_1.flee()
fish_1.hunt()