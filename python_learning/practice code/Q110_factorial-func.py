# Write a function to calculate the factorial of a number and print the result.
def check(num):
    for i in range(2, num):
        if num % i == 0:
            print(i)
check(8)

#alternate
# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     print(fact)