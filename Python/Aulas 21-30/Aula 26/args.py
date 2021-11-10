# *args =   parameter that will pack all arguments into a tuple
#                 useful so that a function can accept a varying amount of arguments

#def add (num1,num2):
#    return num1+num2

def add(*args):
    sum = 0
    args = list(args)
    for i in args:
        sum+=i
    return sum

print(add(10,2,3,4,5))