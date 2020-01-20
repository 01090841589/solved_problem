import sys
sys.stdin = open("탈출.txt")

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

from collections import deque
N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
que = deque()
res = N*M
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'S':
            que.append([i, j, 1, 0])
            visited[i][j] = 1
            MAP[i][j] = '.'
for i in range(N):
    for j in range(M):
        if MAP[i][j] == '*':
            que.append([i, j, 1, 1])
            visited[i][j] = 1

while que:
    y, x, scr, k = que.popleft()
    for c in DIR:
        Y = y+c[0]
        X = x+c[1]
        if 0 <= X < M and 0 <= Y < N:
            if k == 0 and MAP[Y][X] == '.':
                if MAP[Y][X] == '.' and visited[Y][X] == 0:
                    visited[Y][X] = 1
                    que.append([Y, X, scr+1, 0])
            elif k == 0 and MAP[Y][X] == 'D' and MAP[y][x] == '.':
                if res > scr:
                    res = scr
            elif k == 1:
                if MAP[Y][X] == '.':
                    MAP[Y][X] = '*'
                    que.append([Y, X, scr+1, 1])
if res == N*M:
    print("KAKTUS")
else:
    print(res)