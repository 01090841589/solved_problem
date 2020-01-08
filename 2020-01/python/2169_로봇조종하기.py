import sys
sys.stdin = open("로봇조종하기.txt")

DIR = [[0, 1], [1, 0], [0, -1]]
N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]
que = [[0, 0, MAP[0][0]]]
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
res = 0
while que:
    y, x, scr = que.pop()
    if [y, x] == [N-1, M-1]:
        if res < scr:
            res = scr
            continue
    for c in DIR:
        Y = y+c[0]
        X = x+c[1]
        if 0 <= Y < N and 0 <= X < M:
            if visited[Y][X] == 0:
                visited[Y][X] = 1
                que.append([Y, X, scr+visited[Y][X]])
                visited[Y][X] = 0
