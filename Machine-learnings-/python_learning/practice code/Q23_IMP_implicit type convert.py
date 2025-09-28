# 6.Demonstrate implicit type conversion by adding an integer and a float, then print the result.

# Implicit type conversion happens automatically when Python converts one data type to another
# during an operation without the programmer explicitly doing it.

def convert():
    a = 1.2
    b = 7
    c = True
    result = a + b
    result2 = b + c
    print(result)
    print(result2)
convert()

