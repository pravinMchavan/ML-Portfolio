# Write a function that checks if a string is a palindrome and print True or False.

def check(s):
    return s == s[::-1]
print(check("madam"))
        