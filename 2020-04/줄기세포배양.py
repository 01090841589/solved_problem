import sys
sys.stdin = open("줄기세포배양.txt")

from collections import deque
DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
T = int(input())
# T = 1
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    MAP = [[[0, 0, 0] for _ in range(int(K*1.5))] for _ in range(int(K*1.5))]
    cell_past = deque()
    cell_now = deque()
    cells = [list(map(int, input().split())) for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if cells[y][x]:
                MAP[y + K-N][x + K-N][0] = cells[y][x]
                MAP[y + K-N][x + K-N][1] = cells[y][x]+1
                MAP[y + K-N][x + K-N][2] = 1
                cell_now.append([y+K-N, x+K-N])
    for turns in range(K):

        cell_past = cell_now
        cell_now = deque()
        for y, x in cell_past:
            MAP[y][x][1] -= 1
        while cell_past:
            y, x = cell_past.popleft()
            if MAP[y][x][1] > 0:
                cell_now.append([y, x])
            else:
                if MAP[y][x][2] == 1:
                    for c in DIR:
                        Y = y+c[0]
                        X = x+c[1]
                        if MAP[Y][X][2] == 0:
                            MAP[Y][X][0] = MAP[y][x][0]
                            MAP[Y][X][1] = MAP[y][x][0]+1
                            MAP[Y][X][2] = 1
                            cell_now.append([Y, X])
                        elif MAP[Y][X][0]+1 == MAP[Y][X][1] and MAP[Y][X][0] < MAP[y][x][0] and MAP[Y][X][2] == 1:
                            MAP[Y][X][0] = MAP[y][x][0]
                            MAP[Y][X][1] = MAP[y][x][0]+1
                    MAP[y][x][2] = -1
                    MAP[y][x][1] = MAP[y][x][0]-1
                    if MAP[y][x][1] > 0:
                        cell_now.append([y, x])
    print("#{} {}".format(tc, len(cell_now)))
    # [print(MAP[i]) for i in range(K*2)]

