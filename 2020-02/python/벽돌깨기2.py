import sys
sys.stdin = open("벽돌깨기.txt")

import copy

from collections import deque

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def wall_break():
    global res
    MAP_NOW = copy.deepcopy(MAP)
    q = deque()
    for site in code:
        for y in range(H):
            if MAP_NOW[y][site] > 0:
                q.append([y, site])
                while q:
                    Y, X = q.popleft()
                    wid = MAP_NOW[Y][X] - 1
                    MAP_NOW[Y][X] = 0
                    for c in DIR:
                        for j in range(1, wid+1):
                            Y_set = Y+ (c[0]*j)
                            X_set = X+ (c[1]*j)
                            if 0 <= Y_set < H and 0 <= X_set < W:
                                if MAP_NOW[Y_set][X_set] > 0:
                                    q.append([Y_set, X_set])
                            else:
                                break

                for XX in range(W):
                    buf = []
                    for YY in range(H-1, -1, -1):
                        if MAP_NOW[YY][XX] > 0:
                            buf.append(MAP_NOW[YY][XX])
                    for i in range(len(buf)):
                        MAP_NOW[H-i-1][XX] = buf[i]
                    for i in range(len(buf), H):
                        MAP_NOW[H-1-i][XX] = 0
                break

    cnt = 0
    for y in range(H):
        for x in range(W):
            if MAP_NOW[y][x] > 0:
                cnt += 1
    if res > cnt:
        res = cnt
    if res == 0:
        return


def shoot_site(k):
    global res
    if res == 0:
        return
    if k == N:
        wall_break()
        return
    for i in range(W):
        code[k] = i
        shoot_site(k+1)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    MAP = [list(map(int, input().split())) for i in range(H)]
    code = [-1] * N
    res = 1000
    shoot_site(0)
    print("#{} {}".format(tc, res))




