import sys
sys.stdin = open("다리연결.txt")

import collections
import itertools


def findisland(i, j):
    rx, ry = i, j
    R = [rx, ry]
    Q = collections.deque([[i, j]])
    vl[j][i] = 1
    while Q:
        x, y = Q.popleft()
        for dx, dy in d:
            tx, ty = x + dx, y + dy
            if 0 <= tx < N and 0 <= ty < N and M[ty][tx] and not vl[ty][tx]:
                vl[ty][tx] = 1
                Q.append([tx, ty])
                if tx > rx:
                    rx = tx
                if ty > ry:
                    ry = ty
    R = R + [rx, ry]
    return R


def mkb(i, j):
    il1 = il[i]
    il2 = il[j]
    dist = 0
    for k in range(il1[0], il1[2] + 1):
        if il2[0] <= k <= il2[2]:
            if il2[1] > il1[3]:
                dist = il2[1] - il1[3] - 1
                ml[i][j] = dist
                ml[j][i] = dist
                return
            else:
                dist = il1[1] - il2[3] - 1
                ml[i][j] = dist
                ml[j][i] = dist
                return
    for k in range(il1[1], il1[3]+1):
        if il2[1] <= k <= il2[3]:
            if il2[0] > il1[2]:
                dist = il2[0] - il1[2] - 1
                ml[i][j] = dist
                ml[j][i] = dist
                return
            else:
                dist = il1[0] - il2[2] - 1
                ml[i][j] = dist
                ml[j][i] = dist
                return


def combis(k = 0, D = 0):
    global R
    if 0 not in vl2:
        if R > D:
            R = D
        return
    arr = []
    combil = 0
    for i in range(len(ml)):
        if ml[k][i] and not vl2[i]:
            arr.append(i)
    for i in range(1, len(arr)+1):
        combil = itertools.combinations(arr, i)
        if combil:
            for combi in combil:
                for p in combi:
                    vl2[p] = 1
                    D += ml[k][p]
                for q in combi:
                    combis(q, D)
                for p in combi:
                    vl2[p] = 0
                    D -= ml[k][p]


d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    vl = [[0 for _ in range(N)] for _ in range(N)]
    il = []
    R = 0xfffffffff
    for j in range(N):
        for i in range(N):
            if M[j][i] and not vl[j][i]:
                il.append(findisland(i, j))
    ml = [[0 for _ in range(len(il))] for _ in range(len(il))]
    for i in range(len(il)-1):
        for j in range(i+1, len(il)):
            mkb(i, j)
    vl2 = [0]*len(ml)
    vl2[0] = 1
    combis()
    if R == 0xfffffffff:
        R = -1
    print(R)