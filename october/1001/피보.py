import sys
sys.stdin = open("피보.txt")

a, b = 0, 0

fib = [0] * 45
for i in range(45):
    if i < 2:
        fib[i] = 1
    else:
        fib[i] = fib[i-1]+fib[i-2]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        print(fib[N-2], fib[N-1])