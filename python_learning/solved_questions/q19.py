# Input two numbers, print the larger one.

a = int(input("Enter first number:"))
b = int(input("enter second number:"))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{b} is greator then {a}")
else:
    print("Numbers are equal")