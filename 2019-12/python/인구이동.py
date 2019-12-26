import sys
sys.stdin = open("인구이동.txt")

DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]


N, L, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
result = 0
while True:
    MAP2 = [MAP[i][:] for i in range(N)]
    visited = [[0] * N for i in range(N)]
    color = set()
    c = 1
    for y in range(N):
        for x in range(N):
            queue = [[y, x, c]]
            while queue:
                y, x, c = queue.pop(0)
                for arr in DIR:
                    Y = y + arr[0]
                    X = x + arr[1]
                    if 0 <= X < N and 0 <= Y < N:
                        if visited[y][x] == c and visited[Y][X] == c:
                            continue
                        if L <= abs(MAP[Y][X] - MAP[y][x]) <= R:
                            if visited[Y][X] != c:
                                queue.append([Y, X, c])
                            visited[y][x] = c
                            visited[Y][X] = c
            c += 1
    for y in range(N):
        for x in range(N):
            if MAP[y][x] != 0:
                color.add(visited[y][x])
    while color:
        c = color.pop()
        if c == 0:
            continue
        popu = 0
        cnt = 0
        for y in range(N):
            for x in range(N):
                if visited[y][x] == c:
                    popu += MAP[y][x]
                    cnt += 1
        if cnt != 0:
            for y in range(N):
                for x in range(N):
                    if visited[y][x] == c:
                        MAP[y][x] = popu//cnt
    if MAP2 == MAP:
        break
    result += 1
print(result)