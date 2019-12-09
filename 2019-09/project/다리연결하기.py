import sys
sys.stdin = open("다리연결.txt")


import itertools

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(y, x, a):
    global xl, xr, yl, yr
    for c in DIR:
        Y = y+c[0]
        X = x+c[1]
        if 0 <= Y < N and 0 <= X < N and visited[Y][X] == 0 and MAP[Y][X] == 1:
            if xl > X:
                xl = X
            if xr < X:
                xr = X
            if yl > Y:
                yl = Y
            if yr < Y:
                yr = Y
            visited[Y][X] = a
            bfs(Y, X, a)


def search_bridge(a, b):
    [yl1, yr1, xl1, xr1] = island[a]
    [yl2, yr2, xl2, xr2] = island[b]
    for x1 in range(xl1, xr1+1):
        for x2 in range(xl2, xr2+1):
            if x1 == x2:
                flag = 1
                if yl2  >yr1:
                    # for see in range(yr1+1, yl2):
                    #     if MAP[see][x1] == 1:
                    #         flag = 0
                    #         break
                    if flag and [a, b, abs(yl2-yr1-1)] not in bridge:
                        bridge.append([a, b, abs(yl2-yr1-1)])
                if yl1 > yr2:
                    # for see in range(yr2+1, yl1):
                    #     if MAP[see][x1] == 1:
                    #         flag = 0
                    #         break
                    if flag and [a, b, abs(yl1-yr2-1)] not in bridge:
                        bridge.append([a, b, abs(yl1-yr2-1)])
    for y1 in range(yl1, yr1+1):
        for y2 in range(yl2, yr2+1):
            if y1 == y2:
                flag = 1
                if xl2 > xr1:
                    # for see in range(xr1+1, xl2):
                    #     if MAP[y1][see] == 1:
                    #         flag = 0
                    #         break
                    if flag and [a, b, abs(xl2-xr1-1)] not in bridge:
                        bridge.append([a, b, abs(xl2-xr1-1)])
                if xl1 > xr2:
                    # for see in range(xr2+1, xl1):
                    #     if MAP[y1][see] == 1:
                    #         flag = 0
                    #         break
                    if flag and [a, b, abs(xl1-xr2-1)] not in bridge:
                        bridge.append([a, b, abs(xl1-xr2-1)])
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    result = 999999
    a = 0
    island = []
    bridge = []
    for y in range(N):
        for x in range(N):
            if MAP[y][x] == 1 and visited[y][x] == 0:
                xl, xr, yl, yr = x, x, y, y
                a += 1
                visited[y][x] = a
                bfs(y, x, a)
                island.append([yl, yr, xl, xr])
    for i in range(a-1):
        for j in range(i+1, a):
            search_bridge(i, j)



    for A in itertools.permutations(range(len(bridge)), len(bridge)):
        bridge_visited = [0]*a
        scr = 0
        for B in A:
            if result <= scr:
                break
            if sum(bridge_visited) == 0:
                bridge_visited[bridge[B][0]] = 1
            if bridge_visited[bridge[B][0]] == 1 and bridge_visited[bridge[B][1]] == 1:
                continue
            if bridge_visited[bridge[B][0]] == 1 or bridge_visited[bridge[B][1]] == 1:
                bridge_visited[bridge[B][0]] = 1
                bridge_visited[bridge[B][1]] = 1
                scr += bridge[B][2]
        if result > scr and sum(bridge_visited) == len(island):
            result = scr
    if result == 999999:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, result))