# Check if the string is a palindrome.
text = input("Enter a text to check palindrome or not: ").lower()
if text == text[::-1]:
    print("The text is palindrome")
else:
    print("Text is not palindrome")