# 8.	Count character frequency in a string using a dictionary and print the counts.

def counting():
    test = "Hello world"
    count = {}

    for char in test:
        if char in count:
            count[char] +=1
        else:
            count[char] = 1
    for char , freq in count.items():
        print(f"{char}, : {freq}")
counting()