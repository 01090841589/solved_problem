import sys
sys.stdin = open('오셀로.txt')
DIR = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
def put(y, x, k):
    MAP[y][x] = k
    for c in DIR:
        Y = y
        X = x
        cnt = 0
        while True:
            Y += c[0]
            X += c[1]
            if 0 <= Y < N and 0 <= X < N :
                if MAP[Y][X] != k and MAP[Y][X] != 0:
                    cnt += 1
                elif MAP[Y][X] == k:
                    for a in range(cnt):
                        Y -= c[0]
                        X -= c[1]
                        MAP[Y][X] = k
                    break
                elif MAP[Y][X] == 0:
                    break
            else:
                break


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    act = [list(map(int, input().split())) for _ in range(M)]
    MAP = [[0]* N for _ in range(N)]
    MAP[N//2-1][N//2-1], MAP[N//2][N//2] = 2, 2
    MAP[N//2-1][N//2], MAP[N//2][N//2-1] = 1, 1
    for i in act:
        put(i[0]-1, i[1]-1, i[2])
        [print(MAP[i]) for i in range(N)]
        print()
    black, white = 0, 0
    for i in range(N):
        black += MAP[i].count(1)
        white += MAP[i].count(2)
    print('#{} {} {}'.format(tc, black, white))