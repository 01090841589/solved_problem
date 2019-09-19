import sys
sys.stdin = open("최소비용.txt")

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def suffly(y, x, total):
    stack = []
    stack.append([y, x, total])
    while stack:
        y, x, total = stack.pop(0)
        if visit[y][x] < total:
            continue
        for c in DIR:
            Y = y+c[0]
            X = x+c[1]
            if 0 <= X < N and 0 <= Y < N:
                a = MAP[Y][X]-MAP[y][x]
                if a < 0:
                    a = 0
                if visit[Y][X] > total + a + 1:
                    visit[Y][X] = total + a + 1
                    stack.append([Y, X, total + a + 1])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for i in range(N)]
    visit = [[9999999] * N for i in range(N)]
    visit[0][0] = 0
    suffly(0, 0, 0)
    print('#{} {}'.format(tc, visit[N - 1][N - 1]))