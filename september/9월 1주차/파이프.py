import sys
sys.stdin = open('파이프.txt')
PIPE = [[], [[0, 1], [0, -1]], [[1, 0], [-1, 0]], [[1, 0], [0, 1]], [[1, 0], [0, -1]], [[-1, 0], [0, -1]], [[-1, 0], [0, 1]]]
DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def pipe(y, x, score, c, visited, ppipe):
    ppipe += 1
    # print(y, x, DIR[c])
    global result
    if score >= result:
        return
    if y == N-1 and x == N-1:
        # print('도착!', score)
        if DIR[c] == [0, 1]:
            if result > score:
                result = score
            [print(visited[i]) for i in range(N)]
            return
    Y = y+DIR[c][0]
    X = x+DIR[c][1]
    if 0 <= X < N and 0 <= Y < N and MAP[Y][X] != 0 and visited[Y][X] == 0:
        if 0 < MAP[Y][X] < 3:
            if DIR[(c+2)%4] in PIPE[1]:
                for mat in PIPE[1]:
                    if mat != DIR[(c+2)%4]:
                        visited[Y][X] = ppipe
                        pipe(Y, X, score+1, DIR.index(mat), visited, 1)
                        visited[Y][X] = 0
            if DIR[(c+2)%4] in PIPE[2]:
                for mat in PIPE[2]:
                    if mat != DIR[(c+2)%4]:
                        visited[Y][X] = ppipe
                        pipe(Y, X, score+1, DIR.index(mat), visited, 2)
                        visited[Y][X] = 0
        elif 2 < MAP[Y][X] < 7:
            if DIR[(c+2)%4] in PIPE[3]:
                for mat in PIPE[3]:
                    if mat != DIR[(c+2)%4]:
                        visited[Y][X] = ppipe
                        pipe(Y, X, score+1, DIR.index(mat), visited, 3)
                        visited[Y][X] = 0
            if DIR[(c+2)%4] in PIPE[4]:
                for mat in PIPE[4]:
                    if mat != DIR[(c+2)%4]:
                        visited[Y][X] = ppipe
                        pipe(Y, X, score+1, DIR.index(mat), visited, 4)
                        visited[Y][X] = 0
            if DIR[(c+2)%4] in PIPE[5]:
                for mat in PIPE[5]:
                    if mat != DIR[(c+2)%4]:
                        visited[Y][X] = ppipe
                        pipe(Y, X, score+1, DIR.index(mat), visited, 5)
                        visited[Y][X] = 0
            if DIR[(c+2)%4] in PIPE[6]:
                for mat in PIPE[6]:
                    if mat != DIR[(c+2)%4]:
                        visited[Y][X] = ppipe
                        pipe(Y, X, score+1, DIR.index(mat), visited, 6)
                        visited[Y][X] = 0
    else:
        return




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    result = 2500
    for start in PIPE[MAP[0][0]]:
        if start != [0, -1]:
            pipe(0,0,1,DIR.index(start), [[0]*N for _ in range(N)], 0)
    print('#{} {}'.format(tc, result))