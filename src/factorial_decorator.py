class TailRecurseException(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


def recurse(*args, **kwargs):
    raise TailRecurseException(*args, **kwargs)


def tail_call(f):
    def func(*args, **kwargs):
        while True:
            try:
                return f(*args, **kwargs)
            except TailRecurseException as r:
                args = r.args
                kwargs = r.kwargs
            continue

    return func


@tail_call
def factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    recurse(n-1, accumulator=accumulator*n)


print(factorial(1000))

# print a very large number
