import sys
sys.stdin = open('파이프.txt')
PIPE = [[], [[0, 1], [0, -1]], [[1, 0], [-1, 0]], [[1, 0], [0, 1]], [[1, 0], [0, -1]], [[-1, 0], [0, -1]], [[-1, 0], [0, 1]]]
DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def pipe(y, x, score, c):
    global result
    if score >= result:
        return
    if y == N-1 and x == N-1:
        print('도착!', score)
        if result > score:
            result = score
        return
    Y = y+DIR[c][0]
    X = x+DIR[c][1]
    if 0 <= X < N and 0 <= Y < N and MAP[Y][X] != 0:
        if 0 < MAP[Y][X] < 3:
            if DIR[(c+2)%4] in PIPE[1]:
                for mat in PIPE[1]:
                    if mat != DIR[(c+2)%4]:
                        pipe(Y, X, score+1, DIR.index(mat))
            if DIR[(c+2)%4] in PIPE[2]:
                for mat in PIPE[2]:
                    if mat != DIR[(c+2)%4]:
                        pipe(Y, X, score+1, DIR.index(mat))
        elif 2 < MAP[Y][X] < 7:
            if DIR[(c+2)%4] in PIPE[3]:
                for mat in PIPE[3]:
                    if mat != DIR[(c+2)%4]:
                        pipe(Y, X, score+1, DIR.index(mat))
            if DIR[(c+2)%4] in PIPE[4]:
                for mat in PIPE[4]:
                    if mat != DIR[(c+2)%4]:
                        pipe(Y, X, score+1, DIR.index(mat))
            if DIR[(c+2)%4] in PIPE[5]:
                for mat in PIPE[5]:
                    if mat != DIR[(c+2)%4]:
                        pipe(Y, X, score+1, DIR.index(mat))
            if DIR[(c+2)%4] in PIPE[6]:
                for mat in PIPE[6]:
                    if mat != DIR[(c+2)%4]:
                        pipe(Y, X, score+1, DIR.index(mat))
    else:
        return




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    # [print(MAP[i]) for i in range(N)]
    result = 2500
    for start in PIPE[MAP[0][0]]:
        if start != [0, -1]:
            while True:
                pipe(0,0,1,DIR.index(start))
    print('#{} {}'.format(tc, result))