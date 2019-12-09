import sys
sys.stdin = open("유턴싫어.txt")

from collections import deque

DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]


N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
route = deque()
flag = 0
for y in range(N):
    for x in range(M):
        if flag:
            break
        if MAP[y][x] == '.':
            cnt = 0
            for c in DIR:
                Y = y+c[0]
                X = x+c[1]
                if 0 <= Y < N and 0 <= X < M and MAP[Y][X] == '.':
                    cnt += 1
            if cnt < 2:
                flag = 1


if flag:
    print(1)
else:
    print(0)