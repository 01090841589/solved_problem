import sys
sys.stdin = open('보급로.txt')
DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def suffly(y, x, total):
    if y == N - 1 and x == N - 1:
        return
    for c in DIR:
        Y = y + c[0]
        X = x + c[1]
        if 0 <= X < N and 0 <= Y < N:
            if visit[Y][X] > total + MAP[Y][X]:
                visit[Y][X] = total + MAP[Y][X]
                suffly(Y, X, total + MAP[Y][X])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input())) for i in range(N)]
    visit = [[999] * N for i in range(N)]
    visit[0][0] = 0
    suffly(0, 0, 0)
    print('#{} {}'.format(tc, visit[N - 1][N - 1]))