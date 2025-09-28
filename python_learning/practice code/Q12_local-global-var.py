# 4.	Show the difference between global and local variables by printing both inside a function.

a = "a" #global var
def var():
    b = "b"
    print(f"{a} is global variable and {b} is local variable")
var()

# global b  # Declare b as a global variable
