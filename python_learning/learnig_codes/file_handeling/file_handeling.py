#File Handeling
#mode: r - read
#      w - write
#      a - append

# open file
# file = open('g:/repo/python_learning/learnig_codes/file_handeling/example.txt', 'r')



# read file
# file = open('g:/repo/python_learning/learnig_codes/file_handeling/example.txt', 'r')
# content = file.read()  #read entire data
# print(content)
# file.close()   #it is best practice to close file


#read content first line
# file = open('g:/repo/python_learning/learnig_codes/file_handeling/example.txt', 'r')
# content = file.readline() #read first line
# print(content)
# file.close()

#read content all lines in list format
# file = open('g:/repo/python_learning/learnig_codes/file_handeling/example.txt', 'r')
# content = file.readlines() #list entire data
# print(content)
# file.close()


#write to a file  if file will not available it will create
# file = open('g:/repo/python_learning/learnig_codes/file_handeling/example2.txt', 'w')
# file.write("Namaste!, kaise ho?") #it will overide 
# file.close()


#append mode this will not overide
# file = open('g:/repo/python_learning/learnig_codes/file_handeling/example2.txt', 'a')
# file.write("Namaste!, \n achha hu") #it will overide 
# file.close()


#close file using with statement
with open('g:/repo/python_learning/learnig_codes/file_handeling/example2.txt', 'r') as file:
    content = file.read()
    print(content)




#check file availibility
# import os

# file_path = 'g:/repo/python_learning/learnig_codes/file_handeling/example.txt'

# if os.path.exists(file_path):
#     with open(file_path, 'r') as file:
#         content = file.readlines()
#         print(content)
# else:
#     print("❌ File not found at path:", file_path)
