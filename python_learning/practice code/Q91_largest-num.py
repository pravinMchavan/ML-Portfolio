# Find the largest of three numbers and print it.
def find(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(num1)
    elif num2>= num1 and num2 >= num3:
        print(num2)
    else:
        print(num3)
find(5,5,5)
    