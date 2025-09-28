# #----------dictionary in python------------

# #syntax:

# # my_dict = {'key1':'value', 'key2':'value'}

# #creating methods
# #method1 - using curly braces
# # cohort = {'course': 'python', 'Instructor': 'Pravin', 'level': 'beginner' }
# # print(cohort)

# # #method2 - using dict() constructor
# # person = dict(name= "madhav", age= 20, grede = 'a')
# # print(person)

# # #Method3 using list of tuple
# # person2 = dict([('name', 'Madhav'), ('age', 20), ('city','Mumbai')])
# # print(person2)

# #--------access dictionary values----------
# # student = {
# #     1: 'Class-X',
# #     'name': 'Madhav',
# #     'grade': 'A',
# #     'city': 'Mumbai'
# # }
# # print(student['name']) # accessing key value


# #------------dictionary methods------------
# # student = {
# #     1: 'Class-X',
# #     'name': 'Pravin',
# #     'grade': 'A',
# #     'city': 'Mumbai'
# # }
# # #key access
# # print(student.keys())

# # #value access
# # print(student.values())

# # #items
# # print(student.items())

# # #get 
# # print(student.get('name'))


# #------------add / modify dictionary ------------

# # student = {
# #     1: 'Class-X',
# #     'name': 'Pravin',
# #     'grade': 'A',
# #     'city': 'Mumbai'
# # }

# # #add items
# # student['email'] = 'stud@gmail.com'
# # print(student)

# # #modify/replace item - assign operator
# # student['grade'] = 'A+'
# # print(student)

# #remove items
# #del to remove items
# # del student['grade']
# # print(student)

# #pop() method
# # student.pop('grade')
# # print(student)


# #--------------dictionary iterations---------------
# student = {
#     'name': 'Pravin',
#     'grade': 'A',
#     'city': 'Mumbai'
# }

# #loop through keys
# # for x in student:
# #     print(x)  #this will print keys

# # #loop through values
# # for i in student:
# #     print(student[i])

# #using .values() 
# # for i in student.values():
# #     print(i)


# #loop throgh key-value pair
# # for keys,values in student.items():
# #     print(keys, values)



# #--------------Nested dictionary-----------------
# main_stud ={

#     'student1': {'name': 'Madhav', 'age': 25},
#     'student2': {'name': 'Pravin', 'age': 24}
# }

# print(main_stud)


# #access value
# print(main_stud['student1'])
# print(main_stud['student1']['name'])
# print(main_stud['student2']['age'])



# #-----------dictionary comprehension -------------
# #syntax
# #{key_exp = value_exp for item in iterable if conditio}

my_dict = {x:x*x for x in range(1,6)}
print(my_dict)