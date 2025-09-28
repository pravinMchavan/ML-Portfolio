# 2.	Convert a float to an int and an int to a float, then print both results.
a = float(input("Enter a Number="))
b = int(input("Enter a Number="))
def convert():
    c = int(a)
    d = float(b)
    print("befor converting")
    print("type of a ",type(a))
    print("type of b",type(b))
    print("After converting")
    print("type of a ",type(c))
    print( "type of b",type(d))

convert()
