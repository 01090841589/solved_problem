import sys
sys.stdin = open("달이 차오른다.txt")

from collections import deque
DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def moon(y, x, k, keys):
    pass

N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
[print(MAP[i]) for i in range(N)]
visited = [[[123456789]*64 for _ in range(M)] for _ in range(N)]
start, end = [0, 0], [0, 0]
for y in range(N):
    for x in range(M):
        if MAP[y][x] == '0':
            start = [y, x]
        elif MAP[y][x] == '1':
            end = [y, x]
visited[0][start[0]][start[1]] = 0
queue = deque([[start[0], start[1], 0, 0]])
while queue:
    y, x, dis, key = queue.popleft()
    if MAP[y][x] == '1':
        print()
        continue
    for c in DIR:
        Y = y + c[0]
        X = x + c[1]
        if 0 <= Y < N and 0 <= X < M:
            if visited[key][Y][X] > dis+1:
                visited[key][Y][X] = dis+1
                queue.append([Y, X, dis+1, key])

