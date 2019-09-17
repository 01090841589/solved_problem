import sys
sys.stdin = open('청소기.txt')

DIR = [[-1, 0], [0, -1], [1, 0], [0, 1]]




N, M = map(int, input().split())
y, x, k = map(int, input().split())
if k == 1:
    c = 3
elif k == 3:
    c = 1
else:
    c = k

MAP = [list(map(int, input().split())) for _ in range(N)]
flag = 1
result = 0
while flag:
    if MAP[y][x] == 0:
        MAP[y][x] = 2
        result += 1
    for i in range(1, 5):
        Y = y + DIR[(c + i) % 4][0]
        X = x + DIR[(c + i) % 4][1]
        if MAP[Y][X] == 0:
            y = Y
            x = X
            c = (c+i)%4
            break
        if i == 4:
            if MAP[y-DIR[c][0]][x-DIR[c][1]] == 1:
                flag = 0
                break
            else:
                y -= DIR[c][0]
                x -= DIR[c][1]

print(result)