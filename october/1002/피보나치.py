def fibo(n):
    global a, b
    if n == 0:
        a += 1
        return 0
    elif n == 1:
        b += 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

a, b = 0, 0

fib = [0] * 45

fibo(0)
print(a, b)
a, b = 0, 0
fibo(1)
print(a, b)
a, b = 0, 0
fibo(2)
print(a, b)
a, b = 0, 0
fibo(3)
print(a, b)
a, b = 0, 0
fibo(4)
print(a, b)
a, b = 0, 0
fibo(5)
print(a, b)
a, b = 0, 0
fibo(6)
print(a, b)
a, b = 0, 0
fibo(7)
print(a, b)
a, b = 0, 0
fibo(8)
print(a, b)
a, b = 0, 0
fibo(9)
print(a, b)
a, b = 0, 0
fibo(10)
print(a, b)
a, b = 0, 0
fibo(30)
print(a, b)