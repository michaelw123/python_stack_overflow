thunk = lambda func, *args: lambda: func(*args)


def trampoline(func):
    while callable(func):
        func = func()
    return func


def factorial(n, accumulator=1):
    return accumulator if n == 0 else thunk(factorial, n-1, n*accumulator)


factorial_trampoline_thunk = lambda *args: trampoline(factorial(*args))

print(factorial_trampoline_thunk(1000))


def is_even(n):
    if n==0:
        return True
    else:
        return thunk(is_odd, n-1)
def is_odd(n):
    if n==0:
        return False
    else:
        return thunk(is_even, n-1)


is_even_trampoline_thunk = lambda *args: trampoline(is_even(*args))
is_odd_trampoline_thunk = lambda *args: trampoline(is_odd(*args))

print(is_even_trampoline_thunk(1000))
print(is_odd_trampoline_thunk(1000))
