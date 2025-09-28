# 3.	Create a function that returns a sorted version of the list in ascending order.

def sorting(a):
    a.sort()
    return a
print(sorting([1,3,2,4]))


#alternative

def sorting(a):
    return sorted(a)
print(sorting([4,5,4,5]))