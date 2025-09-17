# Return and print the category of BMI based on a given BMI value.
def check(bmi):
    if bmi < 18.7:
        category = "under weight"
    elif bmi < 25:
        category = "normal Weight"
    elif bmi < 30:
        category = "over weight"
    else:
        category = "obese"

    print(f"BMI category :", category)
    return category

check(17)