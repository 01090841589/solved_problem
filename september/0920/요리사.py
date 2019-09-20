import sys
sys.stdin = open("요리사.txt")

from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    result = 99999999
    for As in combinations(range(1, N+1), N//2):
        A = []
        B = []
        A_scr = 0
        B_scr = 0
        for i in range(1, N+1):
            if i in As:
                A.append(i)
            else:
                B.append(i)
        for a in range(N//2):
            for b in range(a+1, N//2):
                A_scr += MAP[A[a]-1][A[b]-1]
                A_scr += MAP[A[b]-1][A[a]-1]
                B_scr += MAP[B[a]-1][B[b]-1]
                B_scr += MAP[B[b]-1][B[a]-1]
        if result > abs(A_scr-B_scr):
            result = abs(A_scr-B_scr)
    print('#{} {}'.format(tc, result))