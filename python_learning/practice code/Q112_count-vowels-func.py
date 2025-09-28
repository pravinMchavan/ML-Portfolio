# Write a function to count vowels in a string and print the count.

def check(s):
    vowels = "aeiouAEIOU"
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    print(count)
check("pravin")