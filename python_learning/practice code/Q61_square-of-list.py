# 10.	Write a function that returns a list of squared values from the original list.

# def square(a):
#     squared = []
#     for i in a:
#         squared.append(i*i)
#     print(squared)

# square([1,2,3,4])

#alternative
def sqaure(a):
    return [i * i for i in a]
print(sqaure([1,2,3,4]))
