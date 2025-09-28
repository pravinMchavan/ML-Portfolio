# functions in python
# create function without parameter
# def greetings():
#     print("welcome to python coding practice")
# # call function
# greetings()


# add two no. in fuction with parameters
# def addition(a,b):
#     result = a + b
#     print("addition of your no:", result)
# addition(5,6)

# functions with return statements
#celsius to fahrenhiet conversion

# def celsius_fahreniet(celsius):
#     fahrenhiet = (celsius * 9/5) + 32
#     return fahrenhiet
# #caling function
# temp_f = celsius_fahreniet(25)
# print(temp_f)

# pass statement
# def anything():
#     pass
# print("hello")

# invices

# def invices(username, amount, duedate):
#     print(f"Hello {username}")
#     print(f"your bill of ${amount} is due on {duedate}")

# invices("pravin", 2, "07/2000")

# caps letters
# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# full_name = (create_name("parvin", "chavan"))
# print(full_name)

# calculator

def get_number( a, b):
    addition = a + b
    return addition
addition2 = get_number(1, 2)
print(addition2)


