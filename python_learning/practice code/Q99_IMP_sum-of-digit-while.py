# Sum the digits of a given number and print the sum.

num = 12
add = 0
while num > 0:
      digit = num % 10
      add += digit
      num = num // 10
print(add)