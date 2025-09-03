# 4.	Use isinstance() to check if a variable is an integer or not, and print the result.

def check():
    value = input("Enter a text: ")
    try:
        value = int(value)
    except ValueError:
        pass  
    if isinstance(value, int):
        print(f"{value} is an integer.")
    else:
        print(f"{value} is NOT an integer.")

check()
