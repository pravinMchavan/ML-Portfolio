# Write a function to generate and print the multiplication table for a given number.

def mult(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")
mult(5)