# Check if a year is a leap year and print "Leap Year" or "Not a Leap Year".

def check(year):
    if year % 100 == 0:
        print(f"{year} not a leap year")
    elif year % 400 == 0:
        print(f"{year} It is a leap year")
    elif year % 4 == 0:
        print(f"{year} is is a leap year")
    else:
        print(f"{year} not a leap year")
check(2025)