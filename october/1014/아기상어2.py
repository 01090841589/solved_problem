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
                    if 0< MAP[Y][X] < shark:
                        buf = visited[y][x] + 1
                        visited[Y][X] = visited[y][x] + 1
                        if target[0] == -1 or target[0] > buf:
                            target[0], target[1], target[2] = [buf, Y, X]
                        elif target[0] == buf:
                            if target[1] > Y:
                                target[0], target[1], target[2] = [buf, Y, X]
                            if target[1] == Y and target[2] > X:
                                target[0], target[1], target[2] = [buf, Y, X]
                    if visited[Y][X] == N*N:
                        queue.append([Y, X])
                        visited[Y][X] = visited[y][x] + 1



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
while True:
    target = [-1, -1, -1]
    distance(shark_yx[0], shark_yx[1])

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