import sys
sys.stdin = open("최소비용.txt")

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def suffly(y, x, total):
    if y == N - 1 and x == N - 1:
        return
    if visit[N-1][N-1] <= total:
        return
    for c in DIR:
        Y = y + c[0]
        X = x + c[1]
        if 0 <= X < N and 0 <= Y < N:
            a = 0
            if MAP[Y][X] > MAP[y][x]:
                a = MAP[Y][X] - MAP[y][x]
            if visit[Y][X] > total + a+1:
                visit[Y][X] = total + a+1
                suffly(Y, X, total + a+1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for i in range(N)]
    visit = [[999] * N for i in range(N)]
    visit[0][0] = 0
    suffly(0, 0, 0)
    print('#{} {}'.format(tc, visit[N - 1][N - 1]))