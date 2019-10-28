import sys
sys.stdin = open("유일한사이클.txt")

def nodelen(i, j):



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        K, L = map(int, input().split())
        MAP[K][L] = 1
        MAP[L][K] = 1

    [print(MAP[i]) for i in range(N+1)]
    print()
    for i in range(1, N):
        for j in range(i+1, N):
            nodelen(i, j)