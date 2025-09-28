# arguments in function
# 1 required arguments
# def greetings(name):  # name is parameter
#     print("hello", name, "!0")
# greetings("pravin") #pravin is argument


# 2 default arguments
# def greetngs(name = "world"): #world is A default argument
#     print("hello", name, "!")
# greetngs()
# greetngs('pravin')

# keyword arguments
# def divide(a, b):
#     return  a / b
# result = divide(100, 20)  # positional argument
# print(result)

# result2 = divide(b = 100, a = 20) #keyword argument
# print(result2)

# 4. arbitrary argument
# arbitrary possitional argument

# def adition(*args):
#     return sum(args)

# result = adition(1, 2, 4)
# print(result)

# def greetings2(*names):
#     for name in names:
#         print(f"Hello {name} !")
# result = greetings2("pravin", "rohit", "kiran")
# print(result)

# 5. arbitrary keyword argument (**kwargs)
# Note : store arguments as dictionary
# def print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_details(name = "pravin", age = 25, city = "mumbai")





    