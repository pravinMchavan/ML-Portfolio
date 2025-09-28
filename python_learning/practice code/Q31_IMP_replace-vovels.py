# 5.Replace all vowels in a string with * and print the modified string.
def rep(a):
    replace=""
    
    for char in a:
        if char.lower() in "aeiou":
            replace += "*"
        else:
            replace +=char
    print(replace)
rep("Pravin")