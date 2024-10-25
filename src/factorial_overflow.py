def factorial(n):
    return 1 if n == 0 else factorial(n - 1) * n

def is_even(n):
    if n==0:
        return True
    else:
        return is_odd(n-1)
def is_odd(n):
    if n==0:
        return False
    else:
        return is_even(n-1)

print(factorial(1000))
print(is_even(1000))

# both functions have stack overflow: RecursionError: maximum recursion depth exceeded in comparison

