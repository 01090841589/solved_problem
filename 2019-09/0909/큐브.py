import sys
sys.stdin = open('큐브.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = 0
    n = N
    a = 0
    b = 1
    A = 0
    if 0 <= N <= 7:
        a += N
    if 8 <= N <= 14:
        A += 7
    if 15 <= N <= 22:
        A += 8
    if 23 <= N <= 49:
        A += 9
    if 50 <= N <= 113:
        A += 10
    if 114<= N <= 329:
        A += 11
    if 330 <= N < 1329:
        A += 12
    if 1330 <= N < 10590:
        A += 13
    if 10590 <= N < 215969:
        A += 14
    if 215970 <= N < 19464802:
        A += 15
    if 19464803 <= N:
        A += 16
    while n > 0:
        if 0 <= N <= 7:
            break
        a = 0

        while N > 0:
            N -= int(N**(1/3))**3
            a += 1
            if a == A:
                N = n
                break
        if a == A:
            N = n
            break
        N = n-b
        b += 1
    if result < a:
        result = a
    print('#{} {} {}'.format(tc, result, N))