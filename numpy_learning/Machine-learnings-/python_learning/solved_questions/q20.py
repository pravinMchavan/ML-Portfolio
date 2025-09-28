# Input marks. Print Grade: >=90: A, >=80: B, >=70: C, else: F

grade = int(input("Enter your marks: "))

if grade >= 90:
    print("your gared is A")
elif grade >= 80:
    print("Your grade is B")
elif grade >= 70:
    print("Your grade is C")
elif grade >=60:
    print("You are failed")
