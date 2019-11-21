def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def fibIt(n):
    if n < 2:
        return n
    fib = 1
    prevFib = 1
    for i in range(2,n):
        temp = fib
        fib +=prevFib 
        prevFib = temp
    return fib

def fibMaster(n, cache=[0,1,1]):
    if n < 2:
        return n
    for i in range(3,n):
        cache.append(cache[i-1] + cache[i-2])
    return cache[-1]

def main():
    print(fib(10))
    print(fibIt(10))
    print(fibMaster(10))

if __name__ == "__main__":
    main()