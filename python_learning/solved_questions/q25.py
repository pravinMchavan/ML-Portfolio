# Input username and password. Allow access if both are correct.

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "pravin" and password == "pravin@123":
    print("login successful")
elif username != "pravin" and password == "pravin@123":
    print("wrong username")
elif username == "pravin" and password != "pravin@123":
    print("wrong passward")
else:
    print("Wrong username and passward")