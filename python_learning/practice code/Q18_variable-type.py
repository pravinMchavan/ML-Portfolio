def type_print():
    text1 = int(input("Enter an integer: "))
    text2 = float(input("Enter a float: "))
    text3 = input("Enter a string: ")
    text4_input = input("Enter True or False: ")

    
    text4 = text4_input.strip().lower() == "true"

    
    print(text1, "is of type:", type(text1))
    print(text2, "is of type:", type(text2))
    print(text3, "is of type:", type(text3))
    print(text4, "is of type:", type(text4))


type_print()
