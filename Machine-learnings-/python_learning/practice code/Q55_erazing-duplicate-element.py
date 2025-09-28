# 4.	Write a function that removes duplicates from a list and prints the new list.

def eraze(a):
    newlit = []
    for i in a:
        if i not in newlit:
             newlit.append(i)
    return newlit
print(eraze(["a","b","a","d"]))