import sys
sys.stdin = open("18224.txt")

from collections import deque

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
n, m = map(int, input().split())
sunmoon = 0
MAP_sun = [[[n*n] * m for __ in range(n)] for _ in range(n)]
MAP_moon = [[[n*n] * m for ___ in range(n)] for _ in range(n)]
MAP = [list(map(int, input().split())) for _ in range(n)]
MAP_sun[0][0][0] = 0
que = deque([[0, 0, 0, 0, 0]])
while que:
    y, x, k, time, day = que.popleft()
    time = time + 1
    if time == m:
        time = 0
        day = (day+1)%2
    for c in DIR:
        Y = y+c[0]
        X = x+c[1]
        if day == 0:
            if 0 <= Y < n and 0 <= X < n:
                if MAP[Y][X] == 0 and MAP_sun[Y][X][time] > k+1:
                    MAP_sun[Y][X][time] = k + 1
                    que.append([Y, X, k+1, time, day])
                if MAP[Y][X] == 1 and time == 0:
                    while True:
                        Y += c[0]
                        X += c[1]
                        if 0 > Y or Y >= n or 0 > X or X >= n:
                            break
                        if MAP[Y][X] == 0:
                            if MAP_sun[Y][X][time] > k+1:
                                MAP_sun[Y][X][time] = k + 1
                                que.append([Y, X, k+1, time, day])
                            break
        elif day == 1:
            if 0 <= Y < n and 0 <= X < n:
                if MAP[Y][X] == 0 and MAP_moon[Y][X][time] > k+1:
                    MAP_moon[Y][X][time] = k + 1
                    que.append([Y, X, k+1, time, day])
                if MAP[Y][X] == 1 and time != 0:
                    while True:
                        Y += c[0]
                        X += c[1]
                        if 0 > Y or Y >= n or 0 > X or X >= n:
                            break
                        if MAP[Y][X] == 0:
                            if MAP_moon[Y][X][time] > k+1:
                                MAP_moon[Y][X][time] = k + 1
                                que.append([Y, X, k+1, time, day])
                            break


result = min(min(MAP_moon[n-1][n-1]), min(MAP_sun[n-1][n-1]))

# [print(MAP_sun[i]) for i in range(n)]
# print()
# [print(MAP_moon[i]) for i in range(n)]
if result == n*n:
    print(-1)
else:
    day = result // (m*2)
    result = result % (m*2)
    if result < m:
        print("{} sun".format(day+1))
    else:
        print("{} moon".format(day+1))