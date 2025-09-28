# Write a function to return the sum of digits of a number and print it.
def adding(num):
    added = 0
    for i in range(1, num+1):
        added += i 
    print(added)
adding(12)