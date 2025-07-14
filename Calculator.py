input("This is a calculator!\nType in two numbers, and see the sum, difference, product, or quotient!\nPress enter to continue! ")
func = input("\nWhat function would you like to use?\nAddition, subtraction, multiplication, or division? ")

#function selection for addition
if func in ["A", "a", "Addition", "addition"]:

    #addition script
    one = input("\nFirst Number: ")
    two = input("Second Number: ")
    sum = float(one) + float(two)
    if sum.is_integer():
        print(f"\nThe sum of {one} and {two} is {int(sum)}!")
    else:
       print(f"\nThe sum of {one} and {two} is {float(sum)}!")
    input()

#function selection for subtraction
elif func in ["S", "s", "Subtraction", "subtraction"]:

    #subtraction script
    one = input("\nFirst Number: ")
    two = input("Second Number: ")
    difference = float(one) - float(two)
    if difference.is_integer():
        print(f"\nThe difference of {one} and {two} is {int(difference)}!")
    else:
       print(f"\nThe difference of {one} and {two} is {float(difference)}!")
    input()

#function selection for multiplication
elif func in ["M", 'm', "Multiplication", "multiplication"]:

    #multiplication script
    one = input("\nFirst Number: ")
    two = input("Second Number: ")
    product = float(one) * float(two)
    if product.is_integer():
        print(f"\nThe product of {one} and {two} is {int(product)}!")
    else:
       print(f"\nThe product of {one} and {two} is {float(product)}!")
    input()

#function selection for division
elif func ["D", 'd', "Division", "division"]:

    #division script
    one = input("\nFirst Number: ")
    two = input("Second Number: ")
    quotient = float(one) / float(two)
    if quotient.is_integer():
        print(f"\nThe quotient of {one} and {two} is {int(quotient)}!")
    else:
       print(f"\nThe quotient of {one} and {two} is {float(quotient)}!")
    input()