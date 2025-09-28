# 2.	Convert a tuple to a list, append an element, then convert back to tuple and print it.

def convert(a, b):
    list1 = list(a)
    list1.append(b)
    tup1 = tuple(list1)
    return tup1
print(convert((1,2,3,4), 5))

