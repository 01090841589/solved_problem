import sys
sys.stdin = open("아기상어.txt")

from collections import deque
DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def distance(y, x):
    queue = deque()
    queue.append([y, x])
    visited = [[N*N]*N for _ in range(N)]
    visited[y][x] = 0
    buf = N*N
    orix, oriy = x, y
    while queue:
        [y, x] = queue.popleft()
        if visited[y][x] >= buf:
            continue
        for c in DIR:
            Y = y + c[0]
            X = x + c[1]
            if 0 <= X < N and 0 <= Y < N:
                if MAP[Y][X] <= shark:
                    if visited[Y][X] > visited[y][x]:
                        queue.append([Y, X])
                        visited[Y][X] = visited[y][x] + 1
                elif MAP[Y][X] == 9:
                    buf = visited[y][x] + 1
                    visited[Y][X] = visited[y][x] + 1
    if target[0] == -1 or target[0] > buf:
        target[0], target[1], target[2] = [buf, oriy, orix]
    elif target[0] == buf:
        if target[1] > oriy:
            target[0], target[1], target[2] = [buf, oriy, orix]
        if target[1] == oriy and target[2] > orix:
            target[0], target[1], target[2] = [buf, oriy, orix]


N = int(input())
MAP =[list(map(int, input().split())) for _ in range(N)]



shark = 2
eats = 0
shark_yx = [-1, -1]
for y in range(N):
    for x in range(N):
        if MAP[y][x] == 9:
            shark_yx = [y, x]

scr = 0
for _ in range(100):
    target = [-1, -1, -1]
    for y in range(N):
        for x in range(N):
            if 0 < MAP[y][x] < shark:
                distance(y, x)
    if target[0] != -1:
        MAP[shark_yx[0]][shark_yx[1]] = 0
        MAP[target[1]][target[2]] = 9
        eats += 1
        if eats == shark and shark < 8:
            shark += 1
            eats = 0
        shark_yx[0], shark_yx[1] = target[1], target[2]
        scr += target[0]
    else:
        break

print(scr)