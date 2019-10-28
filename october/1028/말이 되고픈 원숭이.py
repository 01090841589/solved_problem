import sys
sys.stdin = open("말이되고픈원숭이.txt")

from collections import deque

dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
dirh = [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2] , [-1, 2], [1, -2], [-1, -2]]

def horse_monkey(y, x, k):
    queue = deque()
    queue.append([y, x, k])
    while queue:
        y, x, k = queue.popleft()
        if y == N-1 and x == M-1:
            continue
        if k > 0:
            for c in dirh:
                Y = y+c[0]
                X = x+c[1]
                if 0 <= X < M and 0 <= Y < N and MAP[Y][X] != 1:
                    if visited[Y][X][0] > visited[y][x][0]+1:
                        visited[Y][X][0] = visited[y][x][0]+1
                        visited[Y][X][1] = visited[y][x][1]-1
                        queue.append([Y, X, k-1])
                    elif 0 <= X < M and 0 <= Y < N and visited[Y][X][1] < k:
                        if Y == N-1 and X == M-1:
                            continue
                        if visited[Y][X][0]+((k-visited[Y][X][1])*3) > visited[y][x][0]+1:
                            visited[Y][X][0] = visited[y][x][0]+1
                            visited[Y][X][1] = visited[y][x][1]-1
                            queue.append([Y, X, k])

        for c in dir:
            Y = y+c[0]
            X = x+c[1]
            if 0 <= X < M and 0 <= Y < N and MAP[Y][X] != 1:
                if visited[Y][X][0] > visited[y][x][0]+1:
                    visited[Y][X][0] = visited[y][x][0]+1
                    visited[Y][X][1] = visited[y][x][1]
                    queue.append([Y, X, k])
                elif 0 <= X < M and 0 <= Y < N and visited[Y][X][1] < k:
                    if Y == N-1 and X == M-1:
                        continue
                    if visited[Y][X][0]+((k-visited[Y][X][1])*3) > visited[y][x][0]+1:
                        visited[Y][X][0] = visited[y][x][0]+1
                        visited[Y][X][1] = visited[y][x][1]
                        queue.append([Y, X, k])


K = int(input())
M, N = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[[N*M, 0] for __ in range(M)] for _ in range(N)]
visited[0][0][0] = 0
visited[0][0][1] = K


horse_monkey(0, 0, K)
[print(visited[i]) for i in range(N)]
if visited[N-1][M-1][0] == N*M:
    print(-1)
else:
    print(visited[N-1][M-1][0])