# 8.	Write a function that increments a counter variable and prints the updated value.

counter = 0
def count():
    global counter
    counter += 1
    print(counter)
count()
count()
count()