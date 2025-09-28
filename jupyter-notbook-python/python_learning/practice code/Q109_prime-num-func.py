# Write a function to check if a number is prime and print "Prime" or "Not Prime".

def check(num):
   if num < 2:
      print("not a prime number")
   else:
        for i in range(2, num):
            if num % i == 0:
                print("not a prime number")
                return
        print("prime number")
check(7)