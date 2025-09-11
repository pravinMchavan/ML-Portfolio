# 5.	Find and print the difference between two sets (items in set1 but not in set2).
def dif(a, b):
    new_dif = a.difference(b)
    return new_dif
print(dif({1,2,3}, {1,2,4}))