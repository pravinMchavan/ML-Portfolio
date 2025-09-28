def count_digits(num):
    count = 0
    num = abs(num)   
    if num == 0:
        return 1     
    
    while num > 0:
        num //= 10   
        count += 1
    return count


number = 12345
print("Number of digits:", count_digits(number))

