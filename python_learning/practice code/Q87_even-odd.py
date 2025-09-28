# Write a function to check if a number is even or odd and print "Even" or "Odd"

def check(num):
    if num % 2 == 0:
        print(f"{num} is even number")
    else:
        print(f"{num} is an odd number")

check(34)