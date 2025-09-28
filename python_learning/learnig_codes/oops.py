# #OOPs in python

# #students details using list
# # student_1 = ['Pravin', 10] # name , grade
# # student_2 = ['Vidya', 12] # name , grade

# #using OOPs - creating students record
# #class is a blueprint of an object / template
# class Student:
#     pass

# #object - instance of class / product from blueprint
# student1 = Student()
# print(student1)

# #example
# class Student:
#     def __init__(self, name, grade, percentage):  # init method you have to use it fixed / function is method
#         self.name = name #atribute   #self use to make connection btween class and object
#         self.grade = grade #atribute / properties
#         self.percentage= percentage #atribute
#     def student_details(self): #method
#         print(f"{self.name} is in class {self.grade} and he got {self.percentage} %")

# student1 = Student('Pravin', 11, 20)
# student2 = Student('vidya', 12, 30)
# print(student1.name, student1.grade)

# student1.student_details() 
# student2.student_details()

# #modify object property
# # print(student1.percentage)
# # student1.percentage = 98 #modifying
# # print(student1.percentage)


# # deleting object properties
#     # print(student1.__dict__)
#     # del student1.percentage
#     # print(student1.__dict__)

# # deleting object 
# del student1
# print(student1.__dict__)



# class Student:
#     def __init__(self, name, grade, percentage, team):  # init method you have to use it fixed / function is method
#         self.name = name #atribute   #self use to make connection btween class and object
#         self.grade = grade #atribute / properties
#         self.percentage= percentage #atribute
#         self.team = team
#     def student_details(self): #method
#         print(f"{self.name} is in class {self.grade} and he got {self.percentage} % and he is in {self.team}")

# team1 ='A'
# team2 = 'B'



# student1 = Student('Pravin', 11, 20, team1)
# student2 = Student('vidya', 12, 30, team2)
# # print(student1.name, student1.grade, student1.team)

# student1.student_details() 
# student2.student_details()



# class work:
#         def __init__(self, clean, wash, scrub):
#             self.clean = clean
#             self.wash = wash
#             self.scrub = scrub
    
#         def person(self):
#             print(f"pravin will {self.clean} ramesh will {self.wash} and suman will {self.scrub}")

# worker = work("clean home,", "wash cloths", "scrub dishes,")
# worker.person()



#--------------4. Features in oops------------
#Abstraction
#Encapsulation
#Inheritance
#Polymorphism



#------------F1--Abstraction-------------------

# Abstraction is hiding unnecesarry details from users through classes, methods 


# class Student:
#     def __init__(self, name, grade, percentage, ): 
#         self.name = name
#         self.grade = grade 
#         self.percentage= percentage 
#     def student_details(self):  #method / abstraction
#         print(f"{self.name} is in class {self.grade} and he got {self.percentage + 2} %") # abstraction/ hidden from user

# student1 = Student('Pravin', 11, 95, )
# student2 = Student('vidya', 12, 95, )
# # print(student1.name, student1.grade, student1.team)

# student1.student_details() 
# student2.student_details()


#------------F2--Encapsulation-------------------
#Restricted or prvate access to certain attributes or methods to protect data and enforce controlled access

# class Student:
#     def __init__(self, name, grade, percentage, ): 
#         self.name = name
#         self.grade = grade 
#         self.__percentage= percentage #private #using double underscore __ to make private
# #to access private class we can make method
#     def get_percentage(self):
#         return self.__percentage

# student1 = Student('Pravin', 11, 95, )
# student2 = Student('vidya', 12, 95, )

# #calling private method
# print(student1.get_percentage())




#------------F3--Inheritance-------------------
#allows one class (child) to reuse the prop and methods of another class (parent).

# class Student: #parent class
#     def __init__(self, name, grade, percentage, ): 
#         self.name = name
#         self.grade = grade 
#         self.percentage= percentage 
#     def student_details(self):  #method / abstraction
#             print(f"{self.name} is in class {self.grade} and he got {self.percentage + 2} %")
  
# student1 = Student('Pravin', 11, 95, )
# student2 = Student('vidya', 12, 95, )


# class GraduateStudent(Student):  #GraduateStudent child class inherit properties and methods from Student Parent class
#     def __init__(self, name, grade, percentage, stream): #calling parameters fron parent class and adding new para in child class
#         super().__init__(name, grade, percentage)# calling parent class init
#         self.stream = stream #new atribute in child class

#     def student_details(self):
#                  super().student_details()
       

# Grad_Student1 = GraduateStudent('Rohit', 12, 96, 'PCM')

# print(Grad_Student1.stream) #child class properties printing
# print(student1.name) # parent class properties printing
# Grad_Student1.student_details()




#------------F4--Polymorphism-------------------
#same method new but defferent output
#allows method in defferent classes to have same name but difft behaviours

class Student: #parent class
    def __init__(self, name, grade, percentage, ): 
        self.name = name
        self.grade = grade 
        self.percentage= percentage 
    def student_details(self):  #method / abstraction
            print(f"{self.name} is in class {self.grade} and he got {self.percentage + 2} %")
  
student1 = Student('Pravin', 11, 95, )
student2 = Student('vidya', 12, 95, )


class GraduateStudent(Student):  #child class
    def __init__(self, name, grade, percentage, stream):
        super().__init__(name, grade, percentage)
        self.stream = stream 

    def student_details(self):
        # print(f"{self.name} is in class {self.grade} and he got {self.percentage + 2} %")
        print("same method defferent o/p")
       

Grad_Student1 = GraduateStudent('Rohit', 12, 96, 'PCM')

student1.student_details()
Grad_Student1.student_details()

