# 1.	Write a function that takes a list of numbers and returns the sum.

# def add(a):
#     return sum(a)

# print(add([1,2,3,4]))

# Alternate way to solve

def add(a):
    total = 0
    for i in a:
        total += i;
    return total

print(add([1,2,3,4]))

