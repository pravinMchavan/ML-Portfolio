# 5.Demonstrate the identity operator (is) by comparing two variables and print the result.

def come(a, b):
     print(a is b)   # False: Different objects in memory
     print(a is 1)   # True: Same object in memory 

come(1, 2)