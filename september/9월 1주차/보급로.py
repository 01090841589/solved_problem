import sys
sys.stdin = open('보급로.txt')

DIR = [[0, 1], [1, 0], [-1,0], [0, -1]]

def bfs():
    global cnt, MAP
    que = []
    que.append([0, 0, 0])
    cnt[0][0] = 0
    while que != []:
        x, y, t = que.pop(0)
        if cnt[x][y] < t:
            continue
        for i in DIR:
            nx = x + i[1]
            ny = y + i[0]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if (MAP[nx][ny] > 0):

                if cnt[nx][ny] > cnt[x][y] + MAP[nx][ny]:
                    que.append([nx, ny, t + MAP[nx][ny]])
                    cnt[nx][ny] = cnt[x][y] + MAP[nx][ny]
            else:
                if cnt[nx][ny] > cnt[x][y]:
                    que.append([nx, ny, t])
                    cnt[nx][ny] = cnt[x][y]
    return cnt[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    MAP = []
    N = int(input())
    cnt = [[999] * N for _ in range(N)]
    MAP = [list(map(int, str(input()))) for _ in range(N)]
    print('#{} {}'.format(tc, bfs()))