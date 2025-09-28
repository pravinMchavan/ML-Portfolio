# 1.	Write a function to add an item to a set and print the updated set.

def ad(a):
    a.add("banana")
    return a

print(ad({"apple","mango"}))