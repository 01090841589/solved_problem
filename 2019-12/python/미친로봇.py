from collections import deque
import sys
sys.stdin = open("미친로봇.txt")
DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]



def madrobot(y, x, n, score):
    global total
    if n == 0:
        total += score
    elif n > 0:
        for c in range(4):
            Y = y + DIR[c][0]
            X = x + DIR[c][1]
            if visited[Y][X] == 0:
                visited[Y][X] = 1
                madrobot(Y, X, n-1, score*DIR_per[c])
                visited[Y][X] = 0



n, E, N, W, S = map(int, input().split())
# print(n, E, N, W, S)
DIR_per = [E*0.01, N*0.01, W*0.01, S*0.01]
visited = [[0]*29 for _ in range(29)]
visited[14][14] = 1
total = 0

madrobot(14, 14, n, 1)
# [print(visited[i]) for i in range(29)]
print(total)
