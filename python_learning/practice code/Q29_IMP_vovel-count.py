# 3.Count the number of vowels and consonants in a string and print both counts.
def count(text):
    count = 0
    count2 = 0
    vovel = ["a", "e", "i", "o", "u"]
    consonent = []
    for i in text.lower():
        if i in vovel:
            count +=1
        elif i.isalpha():  # Check that it's a letter (not number/symbol)
            count2 +=1
    print(f"Vovels-{count} and Consenent- {count2}")

count("euieuifejc")