import sys
sys.stdin = open('연산자.txt')
opera = ['+', '-', '*', '/']

def calcu(A, B):
    global MAX, MIN
    while A:
        op = A.pop(0)
        if op == '+':
            B.insert(0, B.pop(0)+B.pop(0))
        elif op == '-':
            B.insert(0, B.pop(0)-B.pop(0))
        elif op == '*':
            B.insert(0, B.pop(0)*B.pop(0))
        elif op == '/':
            x = B.pop(0)
            y = B.pop(0)
            if x < 0:
                x *= -1
                re = x//y
                B.insert(0, re*(-1))
            else:
                B.insert(0, x//y)
    if B[0] > MAX:
        MAX = B[0]
    if B[0] < MIN:
        MIN = B[0]
    del A, B

def perm(n, k, arr):
    global cnt
    if k == n:
        cnt += 1
        calcu(arr[:], nums[:])
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1, arr)
            arr[k], arr[i] = arr[i], arr[k]


N = int(input())
nums = list(map(int, input().split()))
cal = list(map(int, input().split()))
calc = []
cnt = 0
MAX = -999999999999
MIN = 999999999999
for i, j in enumerate(cal):
    if j > 0:
        for _ in range(j):
            calc.append(opera[i])
perm(len(calc), 0, calc)
print(MAX)
print(MIN)
