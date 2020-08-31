import sys
sys.stdin = open('보급로.txt')
DIR = [[1, 0], [0, 1], [0, -1], [-1, 0]]


def BFS():
    global result
    que = [[0, 0, MAP[0][0]]]

    while que:
        y, x, k = que.pop(0)
        # if k >= result:
        #     continue
        if y == N - 1 and x == N - 1:
            if result > k:
                result = k
            continue
        for c in DIR:
            Y = y+c[0]
            X = x+c[1]
            if 0 <= X < N and 0 <= Y < N:
                if pnt[Y][X] > k + MAP[y][x]:
                    que.append([Y, X, k + MAP[y][x]])
                    pnt[Y][X] = k + MAP[y][x]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]
    pnt = [[999] * N for _ in range(N)]
    result = 999
    pnt[0][0] = 0
    BFS()
    print('#{} {}'.format(tc, result))