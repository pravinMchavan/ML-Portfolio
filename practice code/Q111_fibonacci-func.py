# Write a function that returns the nth Fibonacci number and print it.

def fibo(n):
    n1, n2 = 0, 1
    sequence = []
    for i in range(n):
        sequence.append(n1)
        n1, n2 = n2, n1 + n2
    return sequence
print(fibo(10))
        