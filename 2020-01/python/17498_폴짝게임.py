import sys
sys.stdin = open("폴짝게임.txt")

from collections import deque

N, M, D = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[-9999999999]*M for _ in range(N)]
q = deque()
res = -9999999999
for i in range(M):
    q.append([0, i, 0])
    visited[0][i] = 0
for y in range(N-1):
    for x in range(M):
        for dis in range(1, D+1):
            for cnt in range(x-(D-dis), x+(D-dis)+1):
                Y = y+dis
                X = cnt
                if 0 <= Y < N and 0 <= X < M:
                    if visited[Y][X] < visited[y][x] + MAP[y][x]*MAP[Y][X]:
                        visited[Y][X] = visited[y][x] + MAP[y][x]*MAP[Y][X]
                        q.append([Y, X, (visited[y][x] + MAP[y][x]*MAP[Y][X])])
print(max(visited[N-1]))