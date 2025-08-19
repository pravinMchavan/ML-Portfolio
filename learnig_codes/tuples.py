# #tuple in python


# # creating tuples
# #my_tup = (1,2,3)
# # print(my_tup)
# # print(type(my_tup))

# # my_tup2 = (1, "pravin", True, 3.14)
# # print(my_tup2)

# # my_tup3 = 1,2,3
# # print(my_tup3)


# # tuple constructor
# # my_tup4 = tuple((1,5,9))
# # print(type(my_tup4))
# # print(my_tup4)


# #converting list into tuple
# # list1 = [1,2,3,]
# # new_tup = tuple(list1)
# # print(new_tup)

# #create a single  element

# # a = ("a",)# added comma to make tuple
# # print(type(a))

# #access tuple using - indexing
# # fruits = ('apple', 'mango', 'cherry')
# # print(fruits[0])

# #tuple slicing
# # new_tuple = (10,20,30,40,50)
# # print(new_tuple[0:3:1])

# # new_tuple = (10,20,30,40,50)
# # print(new_tuple[0:3:2])


# #---------------Tuple operations------------

# #-------1.concatenation----------
# # tup1 = (1,2,3,4)
# # tup2 = (5,6,7,8)
# # tup3 = (tup1 + tup2)
# # print(tup3)

# #-------2.Repetation----------
# # tup2 = (5,6,7,8)*2
# # tup4 = ('a', 'b')*2
# # print(tup4)

# #-------3.checking for an item----------
# # tup2 = (5,6,7,8)
# # print(1 in tup2)
# # print(5 in tup2)

# #-------4. tuple iteration------------
# # fruits = ('apple', 'mango', 'cherry')
# # for i in fruits:
# #     print(i)

# # i=0
# # while i< len(fruits):
# #     print(fruits[i])
# #     i += 1


# #-------------Tuple Methods-----------------
# #tuple has only two method
# #count 

# # color = ('red', 'green', 'blue', 'green')
# # print(color.count('green'))

# # #index
# # print(color.index('blue'))

# #-----------Tuple functions--------------
# numbers = (2,3,1,4)
# #len()
# print(len(numbers))

# #sum()
# print(sum(numbers))

# #min and max
# print(min(numbers))
# print(max(numbers))

# #sort
# # print(sorted(numbers)) #tuple is now list

# A = sorted(numbers)
# S = tuple(A)
# print(S)


#---------------Pack and unpack--------------------
#pack
# a = "pravin"
# b = 25
# c = "teacher"
# tup_packing = a,b,c
# # print(tup_packing)

# #unpack
# name, age, prof = tup_packing
# print("name is ", name)
# print("age is", age)
# print("prof is ", prof)

#--------------tuple modification-------------
# tup_numbers = (10,20,30)
# # tup_numbers[0]=100 #throw n error
# #how to modify tuple
# list_num = list(tup_numbers)
# print(list_num)
# list_num[0]=100
# print(list_num)
# tupp_numbers = tuple(list_num)
# print(tupp_numbers)

