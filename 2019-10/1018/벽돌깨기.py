import sys
sys.stdin = open("벽돌깨기.txt")


DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
from copy import deepcopy
from collections import deque
def bomb(y, x, maps, k):
    global result
    if result == 0:
        return
    queue = deque()
    queue.append([y, x, maps[y][x]])
    while queue:
        y, x, n = queue.popleft()
        maps[y][x] = 0
        for i in range(1, n):
            for c in DIR:
                Y = y+(c[0]*i)
                X = x+(c[1]*i)
                if 0 <= Y < H and 0 <= X < W and maps[Y][X] > 0:
                    queue.append([Y, X, maps[Y][X]])

    cnt = cascade(maps)
    if cnt == 0 and k >= 0:
        result = cnt
        return
    if k == 0:
        count(maps)
        return
    search(deepcopy(maps), k)

def cascade(maps):
    n = 0
    for i in range(W):
        for j in range(H-1, -1, -1):
            if maps[j][i] == 0:
                for k in range(j-1, -1, -1):
                    if maps[k][i] != 0:
                        maps[j][i], maps[k][i] = maps[k][i], maps[j][i]
                        break
            else:
                n += 1
    return n

def count(maps):
    global result
    cnt = 0
    for i in range(W):
        for j in range(H):
            if maps[j][i] != 0:
                cnt += 1
    if result > cnt:
        result = cnt


def search(smap, k):
    for i in range(W):
        for j in range(H):
            if smap[j][i] != 0:
                bomb(j, i, deepcopy(smap), k-1)
                break


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    result = W*H
    MAP = [list(map(int, input().split())) for _ in range(H)]
    for i in range(W):
        for j in range(H):
            if MAP[j][i] != 0:
                bomb(j, i, deepcopy(MAP), N-1)
                break
    print('#{} {}'.format(tc, result))