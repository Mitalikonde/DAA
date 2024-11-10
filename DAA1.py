
# Write a program non-recursive and recursive program to calculate Fibonacci numbers and analyze their time and space complexity.


def fibonacci(n):
    if n <= 0:
        return 0, 0
    elif n == 1:
        return 1, 1
    elif n == 2:
        return 1, 2

    steps = 2  # Steps start at 2 because we already have the first two terms
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
        steps += 1

    return b, steps

n = int(input("Enter the position in Fibonacci sequence: "))
fib_number, step_count = fibonacci(n)
print(f"Fibonacci number at position {n} is {fib_number} with {step_count} steps.")
