# Count occurrences of a specific element in an array and print the count.

import array
a = array.array('i', [1,2,3,4,4,4])
count = 0
for i in a:
    if i == 4:
        count += 1
print(f"4: {count} ")