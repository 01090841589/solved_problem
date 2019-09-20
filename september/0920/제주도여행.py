import sys
sys.stdin = open("제주도여행.txt")

T = int(input())
for tc in range(1, 2):
    N, M = map(int, input().split())
    MAP = [[0] * N for _ in range(N)]
    for i in range(N-1):
        j = 1
        for a in map(int, input().split()):
            MAP[i][i+j] = a
            MAP[i+j][i] = a
            j += 1
    A = []
    [A.append(list(input().split())) for _ in range(N)]
    print(A)