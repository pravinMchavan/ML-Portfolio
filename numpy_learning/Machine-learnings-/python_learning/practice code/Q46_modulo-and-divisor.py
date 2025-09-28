# 2.	Use modulus (%) and floor division (//) operators on two numbers and print the outputs.

def test(a, b):
    test1 =  a // b   #floor value of division
    test2 =  a % 2 == 0 
    return test1, test2
print(test(18, 7))