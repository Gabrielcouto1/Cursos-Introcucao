#  Higher Order Function =  a function that:
#-----------------------
# 2. returns a function
#-----------------------

def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))