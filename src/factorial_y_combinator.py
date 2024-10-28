y = lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))
y_combinator_thunk = lambda func: (lambda f: (lambda x: x(x))(lambda y: f(lambda *args: lambda: y(y)(*args))))(func)


def y_combinator(func):
  def trampoline(*args):
    f = y_combinator_thunk(func)(*args)
    while callable(f):
      f = f()
    return f
  return trampoline


factorial_y = y( lambda f: lambda n, a: a if not n else f(n-1,a*n) )
print(factorial_y(4,1))

factorial_y_trampoline = y_combinator(lambda f: lambda n, a: a if not n else f(n-1,a*n))
print(factorial_y_trampoline(1000,1))

fibonacci = y_combinator(lambda f: lambda n,p,q: p if not n else f(n-1,q,p+q))

print(fibonacci(1000, 0, 1))


