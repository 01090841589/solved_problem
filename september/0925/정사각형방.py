from collections import deque
import sys
sys.stdin = open('정사각형방.txt')

DIR = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def climb(y, x, n):
    global num, total
    for i in range(4):
        Y = y+DIR[i][0]
        X = x+DIR[i][1]
        if 0 <= Y < N and 0 <= X < N:
            if square[Y][X] == square[y][x]+1:
                visited[Y][X] = visited[y][x]+1
                main_num[Y][X] = main_num[y][x]
                if total <= visited[Y][X]:
                    total = visited[Y][X]
                    if num > main_num[Y][X]:
                        num = main_num[Y][X]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]
    visited = [[1] * N for _ in range(N)]
    main_num = [square[i][:] for i in range(N)]
    total = 1
    num = N
    for a in range(N):
        for b in range(N):
            ori_y, ori_x = a, b
            climb(a, b, 1)
    print('#{} {} {}'.format(tc,num, total))