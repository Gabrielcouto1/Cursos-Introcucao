# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

#def double(x):
#    return x+x;

first_name = "Gabriel"
last_name = "Couto"

double= lambda x: x+x  
multiply = lambda x,y: x*y
full_name = lambda first_name,last_name: first_name+" "+last_name
age_check = lambda age:True if age>=18 else False

print(double(12))
print(multiply(5,4))
print(full_name(first_name,last_name))
print(age_check(19))