# **kwargs =   parameter that will pack all arguments into a dictionary
#                        useful so that a function can accept a varying amount of keyword arguments


#def hello(first,last):
#    print("Hello " + first + " " + last + "!!")
#
#hello(first="Gabriel",last="Couto")


def hello(**kwargs):   
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title="Mr.",First="Gabriel",Middle="Couto",pre_last="de",last="Freitas")