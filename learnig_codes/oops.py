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


class work:
    def __init__(self, clean, wash, scrub):
        self.clean = clean
        self.wash = wash
        self.scrub = scrub
    
    def person(self):
        print(f"pravin will {self.clean} ramesh will {self.wash} and suman will {self.scrub}")

worker = work("clean home,", "wash cloths", "scrub dishes,")
worker.person()
