# exception =   events detected during execution that interrupt the flow of a program

def division():
    try:
        numerator = int(input("Enter a number to divide: "))
        denominator = int(input("Enter a number to divide by: "))
        result = numerator / denominator

    except ZeroDivisionError as e:
        print("\nYou can't divide by zero!")
        print(e)
        print("Try again!\n")
        division()

    except ValueError as e:
        print("\nEnter only numbers please!")
        print(e)
        print("Try again!\n")
        division()

    except Exception as e:
        print("\nSomething went wrong")
        print(e)
        print("\nTry again!\n")
        division()

    else: 
        print("\n{} divided by {} equals to: {}".format(numerator,denominator,result))

division()