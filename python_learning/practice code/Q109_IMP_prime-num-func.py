# Write a function to check if a number is prime and print "Prime" or "Not Prime".
def check(num):
    if num < 2:
        print("not  prime")
        return
            
    for i in range(2, num):
        if num % i == 0:
            print("not prime")
            return
        
    print("prime")
            
check(2)


#alternative 

# def check(num):
#     if num < 2:
#         print("Not Prime")
#         return
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print("Not Prime")
#             return
#     print("Prime")
