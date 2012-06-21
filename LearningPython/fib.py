def fib(n, m={}):
    if n not in m:
        m[n] = 1 if n < 2 else fib(n-1) + fib(n-2)
    return m[n]
    # now print 
print fib(12, {12, 15,56})