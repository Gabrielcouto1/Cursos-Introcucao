# index operator [] = gives access to a sequence’s element (str,list,tuples)

name = "gabriel couto!"

#if (name[0].islower()):
#    name = name.capitalize()

first_name = name[:7].capitalize()
last_name = name[8:-1].capitalize()
last_character = name[-1]

full_name = first_name + last_name + last_character

print("Name: " + name)
print("First name: " + first_name)
print("Last name: " + last_name)
print("Last character: " + last_character)
print("Full name: " + full_name)