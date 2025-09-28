# Take year as input. Check if it's a leap year.

year = int(input("Enter year"))

if (year % 4 ==0 and year % 100 ==0) or (year % 400 ==0):
    print(f"{year} is leap yera")
else:
    print(f"{year} is not a leap yera")

# A year is a leap year if:
# It is divisible by 4
# But not divisible by 100
# Unless it is divisible by 400


