import sys
sys.stdin = open('파이프.txt')
PIPE = [[], [[0, 1], [0, -1]], [[1, 0], [-1, 0]], [[1, 0], [0, 1]], [[1, 0], [0, -1]], [[-1, 0], [0, -1]], [[-1, 0], [0, 1]]]
DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def pipe(y, x, arr, scr):
    global result
    if scr+(N-1-y)+(N-1-x) > result:
        return
    if y == N-1 and x == N-1:
        if result > scr and arr == [0, 1]:
            result = scr
        return
    Y = y+arr[0]
    X = x+arr[1]
    if 0 <= X < N and 0 <= Y < N:
        if 0 < MAP[Y][X] <= 2:
            if visited[Y][X] > scr:
                visited[Y][X] = scr
                pipe(Y, X, arr, scr+1)
                visited[Y][X] = 9999
        elif 2 < MAP[Y][X] <= 6:
            c = DIR.index(arr)
            if visited[Y][X] > scr:
                visited[Y][X] = scr
                pipe(Y, X, DIR[(c+1)%4], scr+1)
                pipe(Y, X, DIR[(c+3)%4], scr+1)
                visited[Y][X] = 9999

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    result = 9999
    visited = [[9999]*N for _ in range(N)]
    visited[0][0] = 0
    if 0 < MAP[0][0] <= 2:
        pipe(0, 0, [0, 1], 1)
    # elif 2 < MAP[0][0] <= 6:
    print('#%s %d' %(tc, result))