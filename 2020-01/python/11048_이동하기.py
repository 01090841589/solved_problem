import sys
sys.stdin = open("이동하기.txt")

from collections import deque
DIR = [[0, 1], [1, 0]]

N, M = map(int,input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
visited[0][0] = MAP[0][0]

que = deque()
que.append([0, 0])
while que:
    y, x = que.popleft()
    for c in DIR:
        Y = y+c[0]
        X = x+c[1]
        if 0 <= Y < N and 0 <= X < M:
            if visited[Y][X] == visited[y][x]+MAP[Y][X]:
                if MAP[Y][X] == 0:
                    visited[Y][X] = visited[y][x]+MAP[Y][X]
                    que.append([Y, X])
            elif visited[Y][X] < visited[y][x]+MAP[Y][X]:
                visited[Y][X] = visited[y][x]+MAP[Y][X]
                que.append([Y, X])
print(visited)

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = data[0][0]

for i in range(N):
    if i == 0:
        for j in range(1, M):
            dp[i][j] = dp[0][j - 1] + data[i][j]

    else:
        for j in range(M):
            if j == 0:
                dp[i][0] = dp[i - 1][0] + data[i][0]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + data[i][j]

print(dp[-1][-1])