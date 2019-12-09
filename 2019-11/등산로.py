DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def mountain(y, x, high, flag, scr):
    global result
    if result < scr:
        result = scr
    for c in DIR:
        Y = y+c[0]
        X = x+c[1]
        if 0 <= X < N and 0 <= Y < N and visited[Y][X] == 0:
            if MAP[Y][X] < high:
                visited[Y][X] = 1
                mountain(Y, X, MAP[Y][X], flag, scr+1)
                visited[Y][X] = 0
            else:
                for i in range(1, K+1):
                    if MAP[Y][X]-i < high and flag:
                        visited[Y][X] = 1
                        mountain(Y, X, MAP[Y][X]-i, 0, scr+1)
                        visited[Y][X] = 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    top = 0
    start = []
    for y in range(N):
        for x in range(N):
            if MAP[y][x] > top:
                start = [[y, x, MAP[y][x]]]
                top = MAP[y][x]
            elif MAP[y][x] == top:
                start.append([y, x, MAP[y][x]])
    result = 0
    visited = [[0]*N for _ in range(N)]
    for c in start:
        visited[c[0]][c[1]] = 1
        mountain(c[0], c[1], c[2], 1, 1)
        visited[c[0]][c[1]] = 0
    print('#{} {}'.format(tc, result))