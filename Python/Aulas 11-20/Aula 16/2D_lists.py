# 2D lists = a list of lists

drinks = ["Coffee ", "Soda ", "Tea "]
dinner = ["Pizza ", "Hamburger ", "Hotdog "]
dessert = ["Cake ", "Ice cream "]

food = [drinks, dinner, dessert]

for row in food:
    for element in row:
        print(element, end= "")
    print()