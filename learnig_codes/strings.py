# # 1. string in python

# # name = "pravin"
# # print(name)
# # print(type(name))
# # print(type("hellow word"))

# ###########2.formating of tring#################
# #1. old mathed with % operator

# # name = "pravin"
# # age = 25
# # print("my name is %s and my age is %d" % (name, age))
# # %s and %d are placeholder for the string and int

# # 2.formated string - str.format()
# # name = "pravin"
# # age = 25
# # print("my name is {} and i am {}".format(name, age))

# # we can also refer variables by index or keywords
# # name = "pravin"
# # age = 25
# # print("my name is {0} and i am {1}".format(name, age))
# # print("my name is {1} and i am {0}".format(name, age))

# # we can assing value of variable in formating
# # print("my name is {name} and i am {age}".format(name = "pravin", age = 25))

# # 3.f-sring formating

# # name = "pravin"
# # age = 25
# # print(f"my name is {name} and i am {age}")

# # we can perform expression inside f-sting
# # name = "pravin"
# # age = 25
# # print(f"my name is {name} and i am {age+5}")


# # escape character 
# # print("hello worold \n my name is pravin \t bye bhail log")



# #-------------------------------------------------------------------

# # string operators
# a = "hello"
# b = "python"

# print(a + b) #concatination

# print(a * 2)#multiple copies

# if "h" in a:
#     print("yess")
# else:
#     print("noo")

# if "H" not in a:
#     print("yess")

# print(r"hello \n world") #supress string


# #---------------------------------------------------------------

# # a = "hello"

# # print(a[1])  # possitive index
# # print(a[1])  #nagative index / if you dont know the no. of string letters and last string letter from last char

# # my_name = "pravin chavan"
# # print(my_name[6]) # it also count blank space


# #------------------------------------------------
# #  string slicing

# name = "pravin"
# print(name[0:4]) #slicing   default step is 1

# print(name[0:4:2]) #jumping or skiping 2 steps

# print(name [4:]) #4rth and forther
# print(name[-1:]) #last char
# print(name[-2:]) #last 2 char
# print(name[0::2]) #every second char
# print(name[:])  #all char
# print(name[::-1]) #reverse string


# #---------------------------------------------
# #  string methods

my_name = "Pravin  "
print(len(my_name))  #lenth of strin
print(my_name.upper()) #capitlize all letters in string
print(my_name.lower()) #conert all letters int small letters
print(my_name.count('a')) #no. of words in string
print(my_name.find('a')) #to find index no. of letter
print(type(my_name.split('a')))# splite the string in two parts output is a list
print(my_name.replace('a','b'))# to replace the string char or string
print(my_name.title()) # capitlize every staring word of string 
print(my_name.strip)  #it delets white space in string

names = ("pravin", "rutik", "kartik")
print(" ".join(names))
print("-".join(names))
