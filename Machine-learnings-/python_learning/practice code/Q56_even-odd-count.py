# 5.	Write a function to count even and odd numbers in a list and print the counts.

def count(a):
    even = 0
    odd = 0
    for i in a:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f"Total Even count:{even}")
    print(f"Total odd count:{odd}")
    return even , odd

count([1,2,3,4,5])

