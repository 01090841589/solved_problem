import sys
sys.stdin = open("로봇조종하기.txt")


from collections import deque
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
value = [[0] * M for _ in range(N)]
queue = deque()
queue.append([0, 0, MAP[0][0]])
visited[0][0] = 1
value[0][0] = MAP[0][0]
while queue:
    y, x, scr = queue.popleft()
    for c in [[0, 1], [1, 0], [0, -1]]:
        Y = y+c[0]
        X = x+c[1]
        if 0 <= Y < N and 0 <= X < M:
            if visited[Y][X] < scr+MAP[Y][X]:
                visited[Y][X] = scr + MAP[Y][X]
                queue.append([Y, X, scr + MAP[Y][X]])
print(MAP[N-1][M-1])