# tuple =   collection which is ordered and unchangeable
#                used to group together related data

student = ("Gabriel", 19, "Male")

#print( student.count("Gabriel") )   # counts how many times the said value ins in the tuple
#print( student.index("Male"))       # returns the position in the tuple the said value is in  

for i in student:
    print(i)

if "Gabriel" in student:
    print("\nGabriel is here!")