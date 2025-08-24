# Write a function find_max(lst) that takes a list of numbers and returns the largest one.

def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num
print(find_max([1,2,3,4]))