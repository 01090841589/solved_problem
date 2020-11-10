import sys
sys.stdin = open("1938.txt")

from collections import deque

def find_tree(tree):
    for y in range(N):
        for x in range(N):
            if MAP[y][x] == tree:
                if 0 <= y+1 < N and MAP[y+1][x] == tree:
                    return y, x, 0
                elif 0 <= x+1 < N and MAP[y][x+1] == tree:
                    return y, x, 1

def check_space(y, x, arr):
    if not arr and 0 <= x-1 and x+1 < N:
        for Y in range(y, y+3):
            if MAP[Y][x-1] or MAP[Y][x+1]:
                break
        else:
            return True
    elif arr and 0 <= y-1 and y+1 < N:
        for X in range(x, x+3):
            if MAP[y+1][X] or MAP[y-1][X]:
                break
        else:
            return True
    return False

def rotate_tree(y, x, arr):
    if arr:
        return y-1, x+1, arr-1
    else:
        return y+1, x-1, arr+1


DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N = int(input())
MAP = [list(input()) for _ in range(N)]
moves = [[[N**3, N**3] for _ in range(N)] for _ in range(N)]
y, x, arr = find_tree('B')
des_y, des_x, des_arr = find_tree('E')
moves[y][x][arr] = 0
q = deque()
q.append([y, x, arr, 0])

for y in range(N):
    for x in range(N):
        if MAP[y][x] == '1':
            MAP[y][x] = 1
        else:
            MAP[y][x] = 0
while q:
    y, x, arr, scr = q.popleft()
    if moves[des_y][des_x][des_arr] <= scr:
        continue
    flag = check_space(y, x, arr)
    if flag:
        ro_y, ro_x, ro_arr = rotate_tree(y, x, arr)
        if moves[ro_y][ro_x][ro_arr] > scr+1:
            moves[ro_y][ro_x][ro_arr] = scr+1
            q.append([ro_y, ro_x, ro_arr, scr+1])
    for c in DIR:
        Y = y+c[0]
        X = x+c[1]
        if 0 <= Y < N and 0 <= X < N:
            if arr:
                if X+2 < N and not MAP[Y][X] and not MAP[Y][X+1] and not MAP[Y][X+2]:
                    if moves[Y][X][arr] > scr+1:
                        moves[Y][X][arr] = scr + 1
                        q.append([Y, X, arr, scr+1])
            else:
                if Y+2 < N and not MAP[Y][X] and not MAP[Y+1][X] and not MAP[Y+2][X]:
                    if moves[Y][X][arr] > scr+1:
                        moves[Y][X][arr] = scr + 1
                        q.append([Y, X, arr, scr+1])
res = moves[des_y][des_x][des_arr]
if res == N**3:
    print(0)
else:
    print(res)