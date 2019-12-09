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
                    for see in range(yr1+1, yl2):
                        if MAP[see][x1] == 1:
                            flag = 0
                            break
                    if flag and [abs(yl2-yr1-1), a, b] not in bridge:
                        bridge.append([abs(yl2-yr1-1), a, b])
                if yl1 > yr2:
                    for see in range(yr2+1, yl1):
                        if MAP[see][x1] == 1:
                            flag = 0
                            break
                    if flag and [abs(yl1-yr2-1), a, b] not in bridge:
                        bridge.append([abs(yl1-yr2-1), a, b])
    for y1 in range(yl1, yr1+1):
        for y2 in range(yl2, yr2+1):
            if y1 == y2:
                flag = 1
                if xl2 > xr1:
                    for see in range(xr1+1, xl2):
                        if MAP[y1][see] == 1:
                            flag = 0
                            break
                    if flag and [abs(xl2-xr1-1), a, b] not in bridge:
                        bridge.append([abs(xl2-xr1-1), a, b])
                if xl1 > xr2:
                    for see in range(xr2+1, xl1):
                        if MAP[y1][see] == 1:
                            flag = 0
                            break
                    if flag and [abs(xl1-xr2-1), a, b] not in bridge:
                        bridge.append([abs(xl1-xr2-1), a, b])

def is_circle(node):
    global total
    if visited[node[1]] == -1 and visited[node[2]] == -1:
        visited[node[1]] = min(node[1], node[2])
        visited[node[2]] = min(node[1], node[2])
        total += node[0]
        return
    if visited[node[1]] != -1 and visited[node[2]] != -1:
        if visited[node[1]] == visited[node[2]]:
            return
        high = max(visited[node[1]], visited[node[2]])
        low = min(visited[node[1]], visited[node[2]])
        for a in range(len(island)):
            if visited[a] == high:
                visited[a] = low
        total += node[0]
    else:
        dis = max(visited[node[1]], visited[node[2]])
        visited[node[1]] = dis
        visited[node[2]] = dis
        total += node[0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    total = 0
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

    bridge.sort()
    visited = [-1]*len(island)
    for k in bridge:
        is_circle(k)
        if visited.count(visited[0]) == len(visited):
            break


    if total == 0:
        print('#{} {}'.format(tc, -1))
    else:
        print('#{} {}'.format(tc, total))