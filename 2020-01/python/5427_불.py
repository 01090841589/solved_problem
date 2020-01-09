import sys
sys.stdin = open("불.txt")

from collections import deque
DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

T = int(input())
for tc in range(1, T+1):
    w, h = map(int, input().split())
    N, M = h, w
    MAP = [list(input()) for _ in range(N)]
    visited = [[N*M] * M for _ in range(N)]
    sangGen = [0, 0]
    que = deque()
    for y in range(N):
        for x in range(M):
            if MAP[y][x] == '*':
                que.append([y, x, 0, 1])
            elif MAP[y][x] == '@':
                sangGen = [y, x, 0, 0]
                visited[y][x] = 0
                MAP[y][x] = '.'
    que.append(sangGen)
    res = N*M+1
    while que:
        y, x, scr, k = que.popleft()
        for c in DIR:
            Y = y+c[0]
            X = x+c[1]
            if 0 <= Y < N and 0 <= X < M:
                if k == 0:
                    if MAP[Y][X] == '.' and visited[Y][X] > visited[y][x]+1:
                        visited[Y][X] = visited[y][x] + 1
                        que.append([Y, X, scr+1, k])
                elif k == 1:
                    if MAP[Y][X] == '.':
                        MAP[Y][X] = '*'
                        que.append([Y, X, scr+1, k])
            elif k == 0:
                if res > scr:
                    res = scr+1
    if res == N*M+1:
        print("IMPOSSIBLE")
    else:
        print(res)