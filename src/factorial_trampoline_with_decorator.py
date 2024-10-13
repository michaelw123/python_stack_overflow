import functools
def trampoline(f):
    def decorated(*args, **kwargs):
        generator = f(*args, **kwargs)
        try:
            generator = next(generator)
        except StopIteration as e:
            init_value = e.value
        return generator

    return decorated


def yields(f, *args, **kwargs):
    generator = f(*args, **kwargs)
    yields_list = [generator]
    while 1:
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

@trampoline
def factorial(n, accumulator=[]):
    if n == 0:
        return functools.reduce(_eval, accumulator, 1)
    yield factorial(n - 1,accumulator=accumulator)

print(factorial(4))