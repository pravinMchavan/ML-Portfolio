# 1.	Write a function that adds, subtracts, and multiplies two numbers and prints the results.

def operation(a, b):
    add = a + b
    sub = a - b
    mult = a * b
    div = a / b
    return add , sub, mult, div
print(operation(6, 4))