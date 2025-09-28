# 4.	Find and print the intersection of two sets.

def inter(a, b):
    new_set = a.intersection(b)
    return new_set
print(inter({1,2,3,4}, {3,4,5,6}))