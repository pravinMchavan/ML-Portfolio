# 4.Use logical operators (and, or, not) in a condition and print the final result.

def logi(a, b):
    if a == 2 and b == 2:
        print("bot are = 2")
    elif (a == 2) or (b == 2):
        print("One of this = 2")
    elif not (a == 2 or a == 2):
        print("None of = 2")

logi(1, 2)