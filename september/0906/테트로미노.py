import sys
sys.stdin = open('테트로미노.txt')
DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def tetmino(y, x, arr, scr, k, load):
    global result
    if k == 4:
        if result < scr:
            result = scr
        return
    for c in range(4):
        Y = y+DIR[c][0]
        X = x+DIR[c][1]
        if 0 <= Y < N and 0 <= X < M and arr != c:
            tetmino(Y, X, (c+2)%4, scr+MAP[Y][X], k+1, load+str(MAP[Y][X]))


def Tspin(y, x, scr):
    global result
    if 0 <= y-1 and 0 <= x-1 and y+1 < N: #ㅓ
        if result < scr + (MAP[y-1][x]+MAP[y][x-1]+MAP[y+1][x]):
            result = scr + (MAP[y-1][x]+MAP[y][x-1]+MAP[y+1][x])
    if x+1 < M and 0 <= x-1 and y+1 < N: #ㅜ
        if result < scr + (MAP[y][x+1]+MAP[y][x-1]+MAP[y+1][x]):
            result = scr + (MAP[y][x+1]+MAP[y][x-1]+MAP[y+1][x])
    if 0 <= y-1 and x+1 < M and y+1 < N: #ㅏ
        if result < scr + (MAP[y-1][x]+MAP[y][x+1]+MAP[y+1][x]):
            result = scr + (MAP[y-1][x]+MAP[y][x+1]+MAP[y+1][x])
    if x+1 < M and 0 <= x-1 and 0 <= y-1: #ㅗ
        if result < scr + (MAP[y][x+1]+MAP[y][x-1]+MAP[y-1][x]):
            result = scr + (MAP[y][x+1]+MAP[y][x-1]+MAP[y-1][x])


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
result = 0
for y in range(N):
    for x in range(M):
        tetmino(y, x, [-1, 0], MAP[y][x], 1, '')
for y in range(N):
    for x in range(M):
        Tspin(y, x, MAP[y][x])
print(result)