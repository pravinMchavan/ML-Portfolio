# 3.	Find and print the union of two sets.

def uni(a, b):
    new = a.union(b)
    return new
print(uni({1,2,3}, {4,5,6}))