name = "Gabriel Couto"

print(len(name))               # will return the lenght of the string
print(name.find("G"))          # will return the position of the letter in the string
print(name.capitalize())       # will capitalize only the first letter of the string
print(name.upper())            # will change all letters to uppercase
print(name.lower())            # will change all letters to lowercase
print(name.isdigit())          # will return false if there is more than numbers and true if its only numbers
print(name.isalpha())          # will return True if there is only letters
print(name.count("o"))         # will return how many specified characteres are there in the string
print(name.replace("o","a"))   # will replace the first argument with the second one
print(name*3)                  # will print x times the string