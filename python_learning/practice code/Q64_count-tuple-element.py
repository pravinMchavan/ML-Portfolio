# 3.Write a function that counts how many times an item appears in a tuple and prints the count.

def check(a, item):
    count = 0
    for i in a:
        if i == item:
            count +=1
    return count
print(check(('a','b','c','a'),('a')))