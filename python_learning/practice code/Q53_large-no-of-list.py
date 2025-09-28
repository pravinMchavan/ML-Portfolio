# 2.	Write a function that finds and returns the largest number in a list.

def check(a):
    if not a:
        return None
    large = a[0]
    for i in a:
        if i > large:
            large = i
    return large

print(check([]))

#Alternate option

# def check(a):
#     return max(a) if a else None

# print(check([1,2,3,4]))