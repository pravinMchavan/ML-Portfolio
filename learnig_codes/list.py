#----------list in python-----

# my_list = [1,2,3]
# print(type(my_list))
# print(my_list)

#list of mixed elements

# my_list2 = [1, "pravin", True , 3.14]
# print(my_list2)

#nasted list

# mylist3 = [1,2,[3,4], True, [5,6,7]]
# print(mylist3)
# print(type(mylist3))


#----------access list - Indexing--------------
# list1 = [10, 20, 30, 40, 50]
# # first element
# print(list1[1])
# #last element
# print(list1[-1])

# list3 = [10, 20, 30, 40, 50, 60, 70,]

#slicing syntax
#list[satre: stop: step]
#first 3 elements
# print(list3[0:3])

# #index 1 to 4
# print(list3[1:5])

#last 3 elemets
# print(list3[-3:])

# #complete list
# print(list3[::])

#alternative elements or steping
# print(list3[::2])

#reverse list
# print(list3[::-1])

#--------------List modification-----------------

# fruits = ["Apple", "Banana", "Blueberry"]

#replace index element at 1
# fruits[1] = "cherry"
# print(fruits)





#--------List method-------------
#1.add element in list at last
# fruits.append("Mango")
# print(fruits)

#----------------------------------

#2.extend the list adding list in another list
# fruits = ["Apple", "Banana", "Blueberry"]
# fruits2 =["mango", "pineapple"]
# fruits.extend(fruits2)
# print(fruits)

#------------------------------------
#3. insert
#inserting with index no.
# fruits.insert(1, "mango")
# print(fruits)

#--------------------------------
#4. remove method
#if elements are repitively it will only remove first element
# fruits.remove("Banana")
# print(fruits)

#--------------------------------
#5. clear
#clear list
# fruits.clear() #empty list
# print(fruits)

#----------------------------------
#6. finding index of element
# index = fruits.index("Banana")
# print(index)

#-----------------------------------
#finding indext whithin a range
# fruits = ["Apple", "Banana", "Blueberry"]
# index = fruits.index("Blueberry", 0 , 3)
# print(index)

#------------------------------
#7. count elements
# count = fruits.count("Banana") # counting how many times is element in list
# print(count)

#-----------------------------
#8 Revrese list
# fruits.reverse() #to reverse list
# print(fruits)

#------------------------------
#9. Sorting list
# numbers = [40, 30, 20, 10]
# numbers.sort()#default sort asc order
# print(numbers)

# fruits.sort()
# print(fruits) #this will sort albhabeticaly

#sorting with a key
# fruits.sort(key=len, reverse=True)
# print(fruits)

#------------------------------------
#10. pop with index value
# numbers = [10, 20, 30, 40]
# popped = numbers.pop(2)
# print(popped) #remove and return an item from a list.  #remove
# print(numbers)

#pop with default
# last = numbers.pop() #it pop last element from list 
# print(last)
# print(numbers)

#11 copying list
# copy_fruits = fruits.copy() #this will shallow fruit list
# print(copy_fruits) 

# #copying list - modifying the copy does not affect the original 
# copy_fruits.append("mango")
# print(copy_fruits)


#---------------Joint list--------------------

list1 = [1,2,3]
list2 = ['a', 'b']

#concotinate using + operator
# final_list = list1 + list2
# print(final_list)


#using append method
# for x in list2:
#     list1.append(x)
# print(list1)


#using extend method
# list1.extend(list2)
# print(list1)


#---------------List Comprehension---------------

# syntax:
# list_name = [expression for item in iterable if condition]

#create a list of square
# square = [x**2 for x in range(1, 6)]
# print(square)

#filter even numbers
# even = [x for x in range(1, 10) if x % 2==0 ]
# print(even)


#------Apply function to each element of a list
# my_list = ['apple', 'mango', 'cherry']
# #print(my_list.upper()) # wrong statement

# uppercase_list = [lit.upper() for lit in my_list]
# print(uppercase_list)

#---------flatten a nested list using list copm-----  IMP
# nested_list = [[1,2], [3,4], [5,6]]

# result = [item for sublist in nested_list for item in sublist]
# print(result)

# def flatten_list(lit):
#     return [item for sublist in lit for item in sublist]
# final_list = flatten_list(nested_list)
# print(final_list)


#----------List iteration -----------
fruits = ['apple', 'mang', 'cherry']
# for fruit in fruits:
#     print(fruit)

#while loop
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1
