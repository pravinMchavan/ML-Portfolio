#Questions based on List, Tuple, Set and dictionary

#Q1. Find the intersection (commom element) of two lits

# list1 = [1,2,3,4]
# list2 = [3,4,5,6]

#using for loop

# def intersection_list(list1, list2):
#     common_list = []
#     for item in list1:
#         if item in list2 and item not in common_list:
#             common_list.append(item)

#     return common_list
# print(intersection_list(list1, list2))


#using list comprehension
# def intersection_list(list1, list2):
#     return [item for item in list1 if item in list2]

# print(intersection_list(list1, list2))

#Q2. Find most frequent Element in a list
