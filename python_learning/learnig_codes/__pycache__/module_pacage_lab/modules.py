#Modules in python
#single py file

#creating a module named with mymodule.py file

# #importing functions
# import mymodule
# mymodule.say_hello("pravin")
# mymodule.say_bye("Ravi")


# #import/use specific part of code
# from mymodule import person1
# print(person1['age'])


#packages: are collection of modules py files with __init__.py file in a folder


#library: collection of modules and packages inbuilt or external
import math

A = 16
print(math.sqrt(A))

#import specific function from lib
from math import factorial
B = 3
print(factorial(B))

#to install online module/lib 
#pip install <library_name>
