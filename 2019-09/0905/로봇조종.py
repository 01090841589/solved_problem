import sys
sys.stdin = open('로봇.txt')

DIR = [[0, 1], [1, 0], [0, -1]]

def bfs():
    global cnt, MAP
    que = []
    que.append([0, 0])
    cnt[0][0] = MAP[0][0]
    while que != []:
        print(que)
        x, y = que.pop(0)
        # if cnt[x][y] > t:
        #     continue
        for i in DIR:
            nx = x + i[1]
            ny = y + i[0]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            print(MAP[ny][nx], MAP[y][x], cnt[ny][nx], ny, nx)
            if MAP[ny][nx]+MAP[y][x] > cnt[ny][nx]:
                cnt[ny][nx] = MAP[ny][nx]+cnt[y][x]
                que.append([ny, nx])
                [print(cnt[i]) for i in range(N)]
            else:
                continue
    return cnt[N - 1][N - 1]


MAP = []
N, M = map(int, input().split())
cnt = [[-999] * M for _ in range(N)]
MAP = [list(map(int, input().split())) for _ in range(N)]
print('#{}'.format(bfs()))
print(cnt)