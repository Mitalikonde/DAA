def fibonacci_iter(n):
    if n < 0:
        return -1, 1, 0  # Invalid input
    if n == 0:
        return 0, 1, 0  # F(0) = 0, sum = 0
    if n == 1:
        return 1, 1, 1  # F(1) = 1, sum = 1

    steps = 0
    a = 0
    b = 1
    fib_sum = a + b  # Initialize the sum with F(0) + F(1)
    for i in range(2, n + 1):
        c = a + b
        fib_sum += c  # Add current Fibonacci number to the sum
        a=b
        b=c
        steps += 1
    return c, steps + 1, fib_sum

def fibonacci_recur(n):
    if n < 0:
        return -1, 1, 0  # Invalid input
    if n == 0:
        return 0, 1, 0  # F(0) = 0, sum = 0
    if n == 1:
        return 1, 1, 1  # F(1) = 1, sum = 1

    # Recursive call for Fibonacci calculation and steps
    fib1, steps1, sum1 = fibonacci_recur(n - 1)
    fib2, steps2, sum2 = fibonacci_recur(n - 2)
   
    # Current Fibonacci number
    fib_n = fib1 + fib2
    total_steps = steps1 + steps2 + 1
   
    # Sum of all Fibonacci numbers up to n
    fib_sum = sum1 + fib2 + fib_n
   
    return fib_n, total_steps, fib_sum

# Main program
if _name_ == '_main_':
    n = int(input("Enter a number: "))
    iter_result, iter_steps, iter_sum = fibonacci_iter(n)
    recur_result, recur_steps, recur_sum = fibonacci_recur(n)

    print("Iterative Fibonacci:", iter_result)
    print("Iterative Steps:", iter_steps)
    print("Iterative Sum:", iter_sum)

    print("Recursive Fibonacci:", recur_result)
    print("Recursive Steps:", recur_steps)
    print("Recursive Sum:", recur_sum)
