import sys
sys.stdin = open("16985.txt")

from itertools import permutations, product
from collections import deque
DIR = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]
def findroad(z, y, x, arr_y, arr_x, k):
    global res
    q = deque()
    q.append([z, y, x, k])
    visited = [[[1] * N for _ in range(N)] for _ in range(N)]
    visited[z][y][x] = 0
    if res == 12:
        return
    while q:
        z, y, x, k = q.popleft()
        if k >= res:
            continue
        if z == 4 and y == arr_y and x == arr_x:
            if res > k:
                res = k
            return
        for c in DIR:
            Z = z+c[0]
            Y = y+c[1]
            X = x+c[2]
            if 0 <= Z < N and 0 <= Y < N and 0 <= X < N:
                if now_maze[Z][Y][X] and visited[Z][Y][X]:
                    visited[Z][Y][X] = 0
                    q.append([Z, Y, X, k+1])
N = 5
res = 999999
maze = []
for z in range(N):
    maze_parts = []
    maze_part = [list(map(int, input().split())) for _ in range(N)]
    rot_maze = [[[0]*N for _ in range(N)] for _ in range(3)]
    for y in range(N):
        for x in range(N):
            if maze_part[y][x]:
                Y, X = y, x
                for k in range(3):
                    YY, XX = X, (N-1)-Y
                    rot_maze[k][YY][XX] = 1
                    Y, X = YY, XX
    maze_parts.append(maze_part)
    for k in range(3):
        maze_parts.append(rot_maze[k])
    maze.append(maze_parts)

for order in permutations(range(N), N):
    for rotate in product([0, 1, 2, 3], repeat=N):
        now_maze = []
        for k in range(N):
            now_maze.append(maze[order[k]][rotate[k]])
        if now_maze[0][0][0] and now_maze[4][4][4]:
            findroad(0, 0, 0, 4, 4, 0)
        elif now_maze[0][0][4] and now_maze[4][4][0]:
            findroad(0, 0, 4, 4, 0, 0)
        elif now_maze[0][4][0] and now_maze[4][0][4]:
            findroad(0, 4, 0, 0, 4, 0)
        elif now_maze[0][4][4] and now_maze[4][0][0]:
            findroad(0, 4, 4, 0, 0, 0)

if res == 999999:
    print(-1)
else:
    print(res)