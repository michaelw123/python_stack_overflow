# Recursion depth maxes out.
def factorial(n):
    return 1 if n ==0 else factorial(n-1) * n


print(factorial(1000))

