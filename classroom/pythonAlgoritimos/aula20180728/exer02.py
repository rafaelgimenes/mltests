# f


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(11))


fb = lambda n: n if n <= 1 else fb(n-1)+fb(n-2)

print(list(map(fb,range(20))))

print(list(map(fib,range(20))))
# gen = (k(x) for x in range(1,5) )
