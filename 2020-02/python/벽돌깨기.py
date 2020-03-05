import sys
sys.stdin = open("벽돌깨기.txt")

import copy

def cascade(Y, X):
    for
    pass

def destroy(row, k):
    if k == 0:
        for y in range(H):
            if MAP1[y][row] > 0:
                cascade(y, row, MAP1[y][row], k)
                break
    elif k == 1:
        pass
    elif k == 2:
        pass
    elif k == 3:
        pass

def wall_game(k, MAP1, MAP2, MAP3, MAP4):
    global res
    if k == 0:
        MAP1 = copy.deepcopy(MAP)
    elif k == 1:
        MAP2 = copy.deepcopy(MAP1)
    elif k == 2:
        MAP3 = copy.deepcopy(MAP2)
    elif k == 3:
        MAP4 = copy.deepcopy(MAP3)
    elif k == 4:
        cnt = 0
        for y in range(H):
            for x in range(W):
                if MAP4[y][x] > 0:
                    cnt += 1
        if res > cnt:
            res = cnt
        return
    for i in range(W):
        destroy(i, k)
        wall_game(k+1, MAP1, MAP2, MAP3, MAP4)


T = int(input())
for tc in range(1, 2):
    N, W, H = map(int, input().split())
    MAP = [list(map(int, input().split())) for i in range(H)]
    res = 1000
    MAP1 = copy.deepcopy(MAP)
    MAP2 = copy.deepcopy(MAP)
    MAP3 = copy.deepcopy(MAP)
    MAP4 = copy.deepcopy(MAP)

    wall_game(0, MAP1, MAP2, MAP3, MAP4)
    print(res)



