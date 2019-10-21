import sys
sys.stdin = open("치즈.txt")

DIR = [[1, 0], [-1, 0], [0, -1], [0, 1]]


from collections import deque
def cheese():
    queue = deque()
    queue.append([0,0])
    visited[0][0] = 1
    while queue:
        [y, x] = queue.popleft()
        for c in DIR:
            Y = y+c[0]
            X = x+c[1]
            if 0<= Y < N and 0 <= X < M and visited[Y][X] == 0:
                visited[Y][X] = 1
                if MAP[Y][X] == 0:
                    queue.append([Y, X])
                elif MAP[Y][X] == 1:
                    MAP[Y][X] = 0

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
result = 0
visited = [[0]*M for _ in range(N)]
cnt = 0
buf = 0

for y in range(N):
    for x in range(M):
        if MAP[y][x] == 1:
            cnt += 1
result = cnt

while cnt > 0:
    buf += 1
    cheese()
    cnt = 0
    for y in range(N):
        for x in range(M):
            visited[y][x] = 0
            if MAP[y][x] == 1:
                cnt += 1
    if cnt > 0:
        result = cnt
print(buf)
print(result)