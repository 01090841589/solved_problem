import sys
sys.stdin = open("주사위.txt")

from collections import deque

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
DICE = [[5, 2, 3, 4], [3, 4, 5, 2], [2, 1, 2, 0], [0, 3, 1 ,3], [4, 0, 4, 1], [1, 5, 0, 5]]
def dice(y, x, k, status):
    global result
    if k >= result:
        return
    if MAP[y][x] == 3 and status == 0:
        if result > k:
            result = k
        return
    for c in range(len(DIR)):
        Y = y+DIR[c][0]
        X = x+DIR[c][1]
        if 0 <= Y < N and 0 <= X < M and MAP[Y][X]:
            if visited[Y][X][DICE[status][c]] > k+1:
                visited[Y][X][DICE[status][c]] = k+1
                dice(Y, X, k+1, DICE[status][c])


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    result = 10000
    start = [0, 0]
    for y in range(N):
        for x in range(M):
            if MAP[y][x] == 2:
                start = [y, x]
    visited = [[[10000, 10000, 10000, 10000, 10000, 10000] for _ in range(M)] for _ in range(N)]
    visited[start[0]][start[1]][0] = 0
    dice = deque()
    dice.append([start[0], start[1], 0, 0])
    while dice:
        y, x, k, status = dice.popleft()
        if k >= result:
            continue
        if MAP[y][x] == 3 and status == 0:
            if result > k:
                result = k
            continue
        for c in range(len(DIR)):
            Y = y+DIR[c][0]
            X = x+DIR[c][1]
            if 0 <= Y < N and 0 <= X < M and MAP[Y][X]:
                if visited[Y][X][DICE[status][c]] > k+1:
                    visited[Y][X][DICE[status][c]] = k+1
                    dice.append([Y, X, k+1, DICE[status][c]])


    # [print(visited[i]) for i in range(N)]
    if result == 10000:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, result))






# 조깅으로 운동한다 온도가 얼마일때 몸이 뜨거워지는가?