#  Higher Order Function =  a function that:
#--------------------------------------
# 1. accepts a function as an argument
#--------------------------------------
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud) # or hello(quiet)