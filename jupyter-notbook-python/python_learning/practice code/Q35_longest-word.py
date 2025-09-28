# 9.Return and print the longest word in a sentence.

def longest():

    words = ("Hi my name is pravin").split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print("longest word is: ", longest_word)

longest()
    
