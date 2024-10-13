import functools


def trampoline(generator):
    return functools.reduce(_eval, *_yields(generator))


def _yields(generator):
    yields_list = [generator]
    while True:
        try:
            generator = next(generator)
            yields_list.append(generator)
        except StopIteration as e:
            init_value = e.value
            break
    yields_list.pop()
    yields_list.reverse()
    return yields_list, init_value


def _eval(value, call):
    try:
        value = call.send(value)
    except StopIteration as e:
        value=e.value
    return value

def factorial(n):
    return 1 if n ==0 else (yield factorial(n - 1)) * n

print(trampoline(factorial(1000)))
