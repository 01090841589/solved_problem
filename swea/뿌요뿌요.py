import sys
sys.stdin = open('puyo.txt')

DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]
colors = ['R', 'G', 'B', "Y"]
def puyo(y, x, color):
    global cnt
    for c in DIR:
        Y = y+c[0]
        X = x+c[1]
        if 0 <= X < 6 and 0 <= Y < 12 and visited[Y][X] == 0:
            if MAP[Y][X] == color:
                visited[Y][X] = 1
                puyo(Y, X, color)
                cnt += 1


def bomb(y, x, color):
    for c in DIR:
        Y = y+c[0]
        X = x+c[1]
        if 0 <= X < 6 and 0 <= Y < 12:
            if MAP[Y][X] == color:
                MAP[Y][X] = '.'
                bomb(Y, X, color)


def cascade():
    for x in range(6):
        ysis = ['.'] * 12
        for y in range(12):
            if MAP[y][x] != '.':
                ysis.append(MAP[y][x])
                ysis.pop(0)
        for y in range(12):
            MAP[y][x] = ysis[y]


MAP = [list(map(str, input())) for i in range(12)]

result = 0
while True:
    flag = 0
    for y in range(12):
        for x in range(6):
            if MAP[y][x] != '.':
                flag += 1
    visited = [[0] * 6 for _ in range(12)]
    for y in range(12):
        for x in range(6):
            if MAP[y][x] != '.' and visited[y][x] == 0:
                cnt = 1
                visited[y][x] = 1
                puyo(y, x, MAP[y][x])
                if cnt >= 4:
                    bomb(y, x, MAP[y][x])
                    MAP[y][x] = '.'
    cascade()
    end_flag = 0
    for y in range(12):
        for x in range(6):
            if MAP[y][x] != '.':
                end_flag += 1
    if flag == 0 or flag == end_flag:
        print(result)
        break
    result += 1