import sys
sys.stdin = open("그래프최소비용.txt")

from collections import deque
import copy
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    node = []
    result = 0
    M = 0
    for y in range(N):
        for x in range(N):
            if MAP[y][x] != 0:
                M += 1
    for k in range(N):
        scr = [999999] * N
        scr[k] = 0
        que = [[k, 0]]
        for _ in range(M-1):
            nowque = copy.deepcopy(que)
            que = []
            for i in nowque:
                for j in range(N):
                    if MAP[i[0]][j] == 0:
                        continue
                    if i[1]+MAP[i[0]][j] < scr[j]:
                        scr[j] = i[1]+MAP[i[0]][j]
                        que.append([j, i[1]+MAP[i[0]][j]])
        print(scr)
    print(node)
