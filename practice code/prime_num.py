# Write a function is_prime(n) that returns True if n is a prime number.

#prime number is only devisible by 1 and itself

def check_prime(num):
    for x in range(2, num):
        if num % x == 0:
            print("Not a prime number")
            break
    else:
        print("Print its a prime number")
           

check_prime(7)