# 2.	Write a function that swaps two variables and prints their values before and after swapping.

def swap(a,b):
    print(f"Befor swapping a = {a} and b = {b}")
    a, b = b, a
    print(f"Afetr swapping a = {a} and b = {b} ")

swap(1, 8)
   
    