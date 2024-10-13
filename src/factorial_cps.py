
def fact_cps(n, cont):
    if n == 0:
        return cont(1)
    else:
        return fact_cps(n - 1, lambda value: cont(n * value))

end_cont = lambda value: value

print(fact_cps(100000, end_cont))