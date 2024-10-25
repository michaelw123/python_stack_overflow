# https://jtauber.com/blog/2008/03/30/thunks,_trampolines_and_continuation_passing/


thunk = lambda func, *args: lambda: func(*args)


def trampoline(func):
    while callable(func):
        func = func()
    return func


def factorial(n, accumulator=1):
    return accumulator if n == 0 else thunk(factorial, n-1, n*accumulator)


factorial_trampoline_thunk = lambda *args: trampoline(factorial(*args))

print(factorial_trampoline_thunk(1000))

# 40238726007709377354370243392...