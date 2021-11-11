# str.format() =    optional method that gives users
#                   more control when displaying output

number = 1_000_000_000_000
pi = 3.14159

print("The number pi is {:.2f}".format(pi))         #only 2 digits of the decimal portion
print("The number is {:,}".format(number))          # automatically places commas where it fits
print("The number is {:b}".format(number))          # prints the number in the binary base
print("The number is {:o}".format(number))          # prints the number in the octadecimal base
print("The number is {:x}".format(number))          # prints the number in the hexadecimal base
print("The number is {:E}".format(number))          # prints the number in the scientific notation