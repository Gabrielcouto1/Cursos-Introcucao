from car import Car

car_1 = Car("Chevy","Corvette",1981,"Black")
car_2 = Car("Ford","Mustang",2012,"Red")

print(car_1.model)
print(car_2.model)

car_2.drive()
car_1.stop()