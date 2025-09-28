# 8.Find and print the frequency of each character in a string.

def freq(a):
    count = {}
    for char in a:
        if char in count:
            count[char] +=1
        else:
            count[char] = 1
    print(count)
freq("madam")