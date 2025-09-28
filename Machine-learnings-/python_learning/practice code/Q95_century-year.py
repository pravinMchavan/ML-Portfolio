# Determine if a year is a century year (divisible by 100) and print "Century Year" or "Not a Century Year".

def check(year):
    if year % 100 == 0:
        print("it is a century year")
    else:
        print("It is not a century year")
check(1001)