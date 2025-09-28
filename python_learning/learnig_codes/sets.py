# #---------------stes in python=-------------
# #charastics of set
# #1. unique values/items
# #2. unordered - no indexing
# #3. mutable - add/remove elements
# #4. immutable elements - replace/modify existings elemets


# #creating a set
# # my_set = {1,2,3}
# # print(my_set)

# # #creating set using constructor
# # my_set2 = set([1,2,3,4])
# # print(my_set2)


# #-----------------set operations-------------
# #adding elemets
# # numbers = {1,2,3,4}
# # numbers.add(100)
# # print(numbers)

# # #remove element
# # fruits = {"apple", "mango", "banana"}
# # # fruits.remove("banana")
# # # print(fruits)
# # fruits.discard("banana")
# # print(fruits)


# #-------------set methods--------------
# #1. union - combine elements from 2 set
# # set1 = {1,2,3}
# # set2 = {3,4,5}
# # set3 = set1.union(set2) # this will aso erage dupiicate element
# # print(set3)
# #alternate
# # set3 = set1 | set2
# # print(set3)

# #2. Intersection - common elements / common elements
# set1 = {1,2,3,4}
# set2 = {3,4,5}
# # inetr_set = set1.intersection(set2)
# # print(inetr_set)
# #alternate
# # inetr_set = set1 & set2
# # print(inetr_set)


# #3. difference - element present in first set only
# #but not in second set

# # set1 = {1,2,3,4}
# # set2 = {3,4,5}
# # diff_set = set1.difference(set2)
# # print(diff_set)

# #alternate
# # diff_set = set1 - set2
# # print(diff_set)


# #4. Symetric difference - element in either set but not in both
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# sdiff_set = set1.symmetric_difference(set2)
# print(sdiff_set) #which elements are in common

# #alternative
# sdiff_set = set1 ^ set2
# print(sdiff_set) #which elements are in common

#------------set itration -------------
# set1 = {1,2,3,4}
# for i in set1:
#     print(i)

#we cant use while loop directly
# i = 0
# while i < len(set1):
#     print(set1[i])
#     i += 1

#-----------set comprehension-------------

squares = {x**2 for x in range(1,6)}
print(squares)