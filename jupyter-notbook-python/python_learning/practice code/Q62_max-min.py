# 1.	Write a function that takes a tuple and returns the maximum and minimum values.

def max_min(a):
    return max(a) , min(a)
    
print(max_min((1,2,3,4)))

#alternative

# maximum, minimum = max_min((1, 2, 3, 4))
# print("Max:", maximum)   # Max: 4
# print("Min:", minimum)   # Min: 1