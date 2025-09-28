#Q1. login credencial 
# user_name = "pravin"
# passward = "pass@123"

# input_name = input("Enter your user name")
# input_passward = input("Enter your user passward")

# if input_name == user_name:
#     if input_passward == passward:
#         print("login successful") 
#     else:
#          print("wrong passward")
# else:
#     print("wrong username")

# Q2 eligibility critaria

math = int(input("enter marks of mathematics: "))
physics = int(input("enter marks of physics: "))
chemistry = int(input("enter marks of chemistry: "))

if (math >= 65 and
    physics >= 55 and
    chemistry >= 50 and
    (math + physics + chemistry) >= 180) or (math + physics) >= 140:
    print("you are eligible")

else:
    print("you are not eligible")