# 6.Check if an element exists in a list using in and print True or False.

def check(a, b):
    for i in a:
        if i in b:
            print(True)
            return
        
    print(False)
check(['a', 'b', 'c'], ['d', 'f', 'a'])


# def check(a, b):
#     print(any(i in b for i in a))
# check(['a', 'b', 'c'], ['d', 'f', 'a'])