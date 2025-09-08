# 9.Write a function to extend a list by another list and print the merged list.

# def murge(a, b):
#     new = a + b
#     print(new)
# murge([1,2,3], [4,5,6])

#alternative

def murge(a, b):
    a.extend(b)
    return a
print(murge([1,2,3], [4,5,6]))