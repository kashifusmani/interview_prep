def fib_1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_1(n-1) + fib_1(n-2)

def fib_2(n, result):
    if n in result:
        return result[n]
    else:
        result[n] = fib_2(n-1, result) + fib_2(n-2, result)
    return result[n]

def fib_3(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b, b+a
    return a

if __name__ == '__main__':
    from time import time
    start = time()
    print(fib_2(10, result = {1:1,2:1}))
    end = time()
    print(end-start)

    start = time()
    print(fib_1(10))
    end = time()
    print(end-start)

    start = time()
    print(fib_3(10))
    end = time()
    print(end-start)