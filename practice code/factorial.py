# Write a function factorial(n) that returns the factorial of a number using a loop.

def factorial(n):
    result = 1
    for i in range(1, n +1):
        result *= i
    return result
print(factorial(10))