# str.format() =    optional method that gives users
#                   more control when displaying output

name = "Gabriel"

print("Hello, my name is {}.".format(name))
print("Hello, my name is {:20}.".format(name))      #enters spaces after the variable
print("Hello, my name is {:<20}.".format(name))     #enter the spaces and the variable stays left
print("Hello, my name is {:>20}.".format(name))     #enter the spaces and the variable stays right 
print("Hello, my name is {:^20}.".format(name))     #enter the spaces and the variable stays centered
