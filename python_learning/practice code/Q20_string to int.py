# 3.	Add two numbers input as strings by converting them to integers first, then print the sum.?

def convert():
    in1 = input("Enter fisr number: ")
    in2 = input("Enter second number: ")
    in1Conv = int(in1)
    in2Conv = int(in2)
    print(in1Conv + in2Conv)

convert()