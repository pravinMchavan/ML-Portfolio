#making calculator project using function

def add (num1 , num2):
    return num1 + num2

def sub (num1 , num2):
    return num1 - num2

def multiplication (num1 , num2):
    return num1 * num2

def division (num1 , num2):
    return num1 / num2

def avg (num1 , num2):
    return ((num1 + num2) / 20)

#user input taking
print("please select operation: \n " 
      "1. Addition\n" 
      "2. Substraction\n" 
      "3. Multiplication\n" 
      "4. Division\n" 
      "5. Avarage")
select = int(input("select oparation from 1,2,3,4,5 :"))

number1 = int(input("Enter a first number"))
number2 = int(input("Enter a second number"))

if select == 1:
    print("addition of two numbers is :", add(number1 , number2))
elif select == 2:
    print("substraction of two numbers is :", sub(number1 , number2))
elif select == 3:
    print("multiplication of two numbers is :", multiplication(number1 , number2))
elif select == 4:
    print("division of two numbers is :", division(number1 , number2))
elif select == 5:
    print("avarage of two numbers is :", avg(number1 , number2))

else:
    print("invalid oparation")