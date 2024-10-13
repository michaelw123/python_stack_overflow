def factorial(n):
    return 1 if n ==0 else factorial(n-1) * n


print(factorial(1000))

#RecursionError: maximum recursion depth exceeded in comparison

