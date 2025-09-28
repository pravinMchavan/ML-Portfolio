# 2.	Check if a given string is a palindrome and print True or False.

def check(a):
    
    if a[::-1] == a:
        print(True)
    else:
        print(False)

check("madam")