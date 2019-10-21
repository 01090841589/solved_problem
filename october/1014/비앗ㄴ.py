import sys
sys.stdin = open("빙산.txt")
DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]


from collections import deque
def island(y, x):
    queue = deque()
    queue.append([y, x])
    visited[y][x] = 1
    while queue:
        [y, x] = queue.popleft()
        for c in DIR:
            Y = y + c[0]
            X = x + c[1]
            if 0 <= Y < N and 0 <= X < M and MAP[Y][X] > 0 and visited[Y][X] == 0:
                visited[Y][X] = 1
                queue.append([Y, X])

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
scr = 0
cnt = 0
visited = [[0] * M for _ in range(N)]
for y in range(N):
    for x in range(M):
        if MAP[y][x] > 0 and visited[y][x] == 0:
            island(y, x)
            cnt += 1


while cnt == 1:
    scr += 1
    visited = [[0]*M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if MAP[y][x] > 0:
                for c in DIR:
                    Y = y-c[0]
                    X = x-c[1]
                    if 0 <= Y < N and 0 <= X < M and MAP[Y][X] == 0:
                        visited[y][x] += 1
    for y in range(N):
        for x in range(M):
            MAP[y][x] -= visited[y][x]
            if MAP[y][x] < 0:
                MAP[y][x] = 0
            visited[y][x] = 0
    cnt = 0
    for y in range(N):
        for x in range(M):
            if MAP[y][x] > 0 and visited[y][x] == 0:
                island(y, x)
                cnt += 1
    if cnt == 0:
        scr = 0
        break
    if cnt != 1:
        break
print(scr)