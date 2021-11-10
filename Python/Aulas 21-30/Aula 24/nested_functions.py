# nested functions calls =  function calls inside other function calls
#                           innermost function calls are resolved first
#                           returned value is used as argument for the next outer function

#number = input("Enter a whole positive number: ")
#number = float(number)
#number = abs(number)
#number = round(number)
#print(number)

# you have to call the functions as the first to be called has to be in the inner position of the line

print(round(abs(float(input("Enter a whole positive number: ")))))