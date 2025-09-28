# Take name and age as input. Print: "<name> will be 30 in <years> years."

name = input("Enter your name: ")
year = int(input("Enter you birth year"))

current_age = 2025 - year

remaining_year = 30 - current_age

print(f"{name} will be 30 in {remaining_year} years")


# if current_age < 30:
#     years_until_30 = 30 - current_age
#     print(f"{name} will be 30 in {years_until_30} years.")
# elif current_age == 30:
#     print(f"{name} is 30 years old this year.")
# else:
#     years_over_30 = current_age - 30
#     print(f"{name} turned 30 {years_over_30} years ago.")