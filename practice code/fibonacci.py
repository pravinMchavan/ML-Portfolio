# Write a function fibonacci(n) that returns the first n numbers in the Fibonacci sequence.
#solve again


def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

print(fibonacci(10))

