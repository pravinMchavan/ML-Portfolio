# Write a program to determine a grade from marks and print the grade (e.g., A, B)

def check(marks):
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 40:
        print("Grade: D")
    else:
        print("Grade: F (Fail)")
check(80)