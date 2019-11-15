import sys
sys.stdin = open("다리연결하기.txt")

from collections import deque
DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def island(y, x, k):
    que = deque([[y, x, k]])
    while que:
        y, x, k = que.popleft()
        for c in DIR:
            Y = y+c[0]
            X = x+c[1]
            if 0 <= Y < N and 0 <= X < M and MAP[Y][X] and visited[Y][X] == 0:
                visited[Y][X] = k
                que.append([Y, X, k])

def bridge(y, x, k):
    for c in DIR:
        n = 0
        while True:
            n += 1
            Y = y+c[0]*n
            X = x+c[1]*n
            if 0 <= Y < N and 0 <= X < M:
                if MAP[Y][X] and n < 3:
                    break
                elif MAP[Y][X] and visited[y][x] != visited[Y][X]:
                    if dist[visited[y][x]][visited[Y][X]] > n-1:
                        dist[visited[y][x]][visited[Y][X]] = n-1
                        dist[visited[Y][X]][visited[y][x]] = n-1
                    break
                elif MAP[Y][X]:
                    break
            else:
                break

def base(n):
    if UF[n] == n:
        return n
    return base(UF[n])

def union(n1, n2, n3):
    global on, result
    bn1 = base(n1)
    bn2 = base(n2)
    if bn1 == bn2:
        return
    if bn1 == n1 and bn2 == n2:
        UF[n2] = n1
        on += 1
        result += n3
        return
    elif bn1 == n1:
        UF[n1] = bn2
        on += 1
        result += n3
        return
    elif bn2 == n2:
        UF[n2] = bn1
        on += 1
        result += n3
        return
    if bn1 != bn2:
        if bn1 > bn2:
            for i in range(k+1):
                if UF[i] == bn1:
                    UF[i] = bn2
        elif bn1 < bn2:
            for i in range(k+1):
                if UF[i] == bn2:
                    UF[i] = bn1
        on += 1
        result += n3
        return


N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
node = []
k = 0
for y in range(N):
    for x in range(M):
        if MAP[y][x] and visited[y][x] == 0:
            k += 1
            visited[y][x] = k
            island(y, x, k)

dist = [[100] * (k+1) for _ in range(k+1)]
for y in range(N):
    for x in range(M):
        if MAP[y][x]:
            bridge(y, x, visited[y][x])
for i in range(1, k+1):
    for j in range(i+1, k+1):
        if dist[i][j] != 100:
            node.append([i, j, dist[i][j]])
node.sort(key=lambda a:a[2])
UF = [i for i in range(k+1)]
on = 0
result = 0
for c in node:
    if on == k-1:
        break
    union(c[0], c[1], c[2])
if result == 0 or on < k-1:
    result = -1

print(result)