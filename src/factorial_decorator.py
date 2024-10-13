class TailRecurseException(Exception):
  def __init__(self, *args, **kwargs):
    self.args = args
    self.kwargs = kwargs


def recurse(*args, **kwargs):
    raise TailRecurseException(*args, **kwargs)


def tail_recursive(f):
  def decorated(*args, **kwargs):
    while True:
      try:
        return f(*args, **kwargs)
      except TailRecurseException as r:
        args = r.args
        kwargs = r.kwargs
        continue

  return decorated
# Normal recursion depth maxes out at 980, this one works indefinitely
@tail_recursive
def factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    recurse(n-1, accumulator=accumulator*n)


print(factorial(1000))