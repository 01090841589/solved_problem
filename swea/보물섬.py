import sys
sys.stdin = open("보물섬.txt")
DIR = [[0, 1], [0, -1], [-1, 0], [1, 0]]
def search_is(y, x, k):
    global result
    queue.append([y, x])

    while queue:
        y, x = queue.pop(0)
        for c in DIR:
            Y = y+c[0]
            X = x+c[1]
            if 0 <= Y < N and 0 <= X < M:
                if MAP[Y][X] == 'L' and visited[Y][X] == 0:
                    visited[Y][X] = visited[y][x] + 1
                    queue.append([Y, X])
        if queue == []:
            if result < visited[y][x]-1:
                result = visited[y][x]-1



N, M = map(int, input().split())

MAP = [list(input()) for _ in range(N)]
result = 0
queue = []
for y in range(N):
    for x in range(M):
        if MAP[y][x] == 'L':
            visited = [[0]*M for _ in range(N)]
            visited[y][x] = 1
            search_is(y, x, 0)
print(result)