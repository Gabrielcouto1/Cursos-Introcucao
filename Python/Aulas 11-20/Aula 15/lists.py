# list = used to store multiple items in a single variable

food = ["pizza", "hotdog", "pasta", "eggs"]

# some functions with lists:

#food.append("ice cream")    #add the item in the end of the list
#food.remove("hotdog")       #removes the said item
#food.pop()                  #removes the last item in the list
#food.insert(0,"cake")       # == food[0]="cake"
#food.clear()                #clears the list
food.sort()                  #sorts the list

for i in food:
    print(i)