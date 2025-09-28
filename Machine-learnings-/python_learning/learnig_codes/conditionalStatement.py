# if condition

# age = 20
# if age > 19:
#     print("You are an adult")

# age = int(input("Enter you age: "))
# if age > 19:
#     print("you are an adult")

# if else condition

# age = int(input("Enter you age: "))
# if age > 19:
#     print("you are an adult")
# else:
#     print("you are not an adult")

# temp = 23
# if temp < 23:
#     print("its a cool day")
# else:
#     print("its a hot day")

# if else else
# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Grade - A+")
# elif marks >= 80:
#     print("Grade - A")
# elif marks >= 70:
#     print("Grade - B+")
# else:
#     print("not a good grade")

# nestad if else statement

# number = int(input("Enter any number"))
# if number > 0:
#     if number % 2 == 0:
#         print("nuber is possitive and even no. ")
#     else:
#         print("nuber is possitive and odd no. ")
# else:
#     if number == 0:
#         print("this is zero")
#     else:
#         print("number is nagative")

# conditional expression (ternary oprator)

# age = 26
# status = "Major" if age >= 26  else "minor"
# print(status)

# Q1. 
# value = None
# if value:
#     print("value is true")
# else:
#     print("value is false")

# Q2. given year is leap year or not

year = int(input("Ener year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f" {year} is leap year")
else:
    print(f"{year}it is leap year")



