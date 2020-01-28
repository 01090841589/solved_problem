import sys
sys.stdin = open("전략게임.txt")

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[[999999] * 16 for _ in range(N)] for _ in range(N)]
    A, B, C = map(int, input().split())
    CodeActive = [0]*16
    for _ in range(A):
        password = list(map(int, input().split()))
        CodeActive[password[0]*8+password[1]*4+password[2]*2+password[3]] = 1
    for _ in range(B):
        password = list(map(int, input().split()))
        CodeActive[password[0]*8+password[1]*4+password[2]*2+password[3]] = 2
    for _ in range(C):
        password = list(map(int, input().split()))
        CodeActive[password[0]*8+password[1]*4+password[2]*2+password[3]] = 3
    result = 999999
    q = deque([[0, 0, 0, 0, 0, 0]])
    while q:
        y, x, code, k, bonus, step = q.popleft()
        if result <= k:
            continue
        if y == N-1 and x == N-1:
            if result > k:
                result = k
        for c in DIR:
            Y = y+c[0]
            X = x+c[1]
            if 0 <= Y < N and 0 <= X < N:
                check = ((code << 1)+MAP[Y][X])%16
                if CodeActive[check] == 1 and step > 2:
                    check = MAP[0][0]
                    if k + 1 - bonus < visited[0][0][check]:
                        visited[0][0][check] = k + 1 - bonus
                        q.append([0, 0, check, k+1 - bonus, 0, 1])
                elif CodeActive[check] == 2 and step > 2:
                    check = 0
                    if k + 1 - bonus < visited[(N//2)-1][(N//2)-1][check]:
                        visited[(N // 2) - 1][(N // 2) - 1][check] = k + 1 - bonus
                        q.append([(N//2)-1, (N//2)-1, check, k+1 - bonus, 0, 0])
                elif CodeActive[check] == 3 and step > 2:
                    check = 0
                    if k + 1 - bonus < visited[Y][X][check]:
                        visited[Y][X][check] = k + 1 - bonus
                        q.append([Y, X, check, k+1 - bonus, 1, 0])
                else:
                    if k + 1 - bonus < visited[Y][X][check]:
                        visited[Y][X][check] = k + 1 - bonus
                        q.append([Y, X, check, k+1 - bonus, 0, step+1])

    print(result)