# Count vowels in a string and print the total count.

vowels = "aeiouAEIOU"
name = "Pravin chavan"
count = 0
for i in name:
    if i in vowels:
        count += 1
print(count)