# Count number of vowels in a string.

text = input("Enter text to count vowels: ")
vowels = ["a", "e", "i", "o", "u"]
count = 0
for char in text.lower():
    if char in vowels:
        count += 1

print("Total vowels : ", count)

