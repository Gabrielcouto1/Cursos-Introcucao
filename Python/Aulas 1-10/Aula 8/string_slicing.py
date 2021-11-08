# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Gabriel Couto"

first_name = name[:7]
last_name = name[7:]
funky_name = name[ : :2]
reversed_name = name[::-1]

print("Full name: " + first_name + last_name)
print("Skipping 2 letters: " + funky_name)
print("Reversed name: " + reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])