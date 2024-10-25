# https://jtauber.com/blog/2008/03/30/thunks,_trampolines_and_continuation_passing/
# https://eli.thegreenplace.net/2017/on-recursion-continuations-and-trampolines
# https://baruchel.github.io/blog/python/2015/07/10/continuation-passing-style-in-python/
# https://github.com/baruchel/tco

thunk = lambda func, *args: lambda: func(*args)
def trampoline(func):
    while callable(func):
        func = func()
    return func


def factorial(n, cont=lambda x: x):
    if n == 0:
        return cont(1)
    else:
        return thunk(factorial, n-1, lambda value: lambda: cont(n * value))

def factorial_cps(n):
    return trampoline(lambda: factorial(n))

def is_even(n, cont=lambda x:x):
    return True if n == 0 else thunk(is_odd, n-1, lambda value: lambda: cont(value-1))
def is_odd(n, cont=lambda x:x):
    return False if n == 0 else thunk(is_even, n-1, lambda value: lambda: cont(value-1))

def is_even_cps(n):
    return trampoline(lambda: is_even(n))

def is_odd_cps(n):
    return trampoline(lambda: is_odd(n))

print(factorial_cps(1000))
print(is_even_cps(1000))
print(is_odd_cps(1000))
