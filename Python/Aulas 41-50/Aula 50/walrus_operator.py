# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

#happy = True
#print(happy)
#
#print(happy:=True)



#while True:
#    food = input("What food do you like?: ").lower()
#
#    if food == "quit":
#        break
#    foods.append(food)

foods = list()
while food := input("What food do you like?: ").capitalize() !="Quit":
    foods.append(food)