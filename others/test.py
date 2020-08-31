import sys
sys.stdin = open('test.txt')
#c 상 하 좌 우
DIR = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def command(y, x, k, c):
    global flag, four_go
    if MAP[y][x] == '<':
        return y, x-1, k, 2
    elif MAP[y][x] == '^':
        return y-1, x, k, 0
    elif MAP[y][x] == '>':
        return y, x+1, k, 3
    elif MAP[y][x] == 'v':
        return y+1, x, k, 1
    elif MAP[y][x] == '_':
        if k == 0:
            return y, x+1, k, 3
        else:
            return y, x-1, k, 2
    elif MAP[y][x] == '|':
        if k == 0:
            return y+1, x, k, 1
        else:
            return y-1, x, k, 0
    elif MAP[y][x] == '-':
        a = k-1
        if a < 0:
            a = 15
        return y+DIR[c][0], x+DIR[c][1], a, c
    elif MAP[y][x] == '+':
        return y+DIR[c][0], x+DIR[c][1], (k+1)%16, c

    elif MAP[y][x] == '?':
        four_go = 1
        return y, x, k, c
    elif MAP[y][x] == '.':
        return y+DIR[c][0], x+DIR[c][1], k, c
    elif MAP[y][x] == 'x':
        if c == 0:
            return R, x, k, c
        elif c == 1:
            return 1, x, k, c
        elif c == 2:
            return y, C, k, c
        elif c == 3:
            return y, 1, k, c
    elif '0' <= MAP[y][x] <= '9':
        return y+DIR[c][0], x+DIR[c][1], int(MAP[y][x]), c
    elif MAP[y][x] == '@':
        flag = 1
        return y, x, k, c




T = int(input())
for tc in range(1, T+1):
    R, C = map(int, input().split())
    MAP = [['x'] + list(map(str, input())) + ['x'] for _ in range(R)]
    MAP.insert(0, ['x'] * (C + 2))
    MAP.append(['x'] * (C + 2))
    # [print(MAP[i]) for i in range(R+2)]
    y, x, k, c = 1, 1, 0, 3
    flag, four_go = 0, 0
    go_list = [[y, x, k, c]]
    for aa in range(R*C*10):
        golist = go_list.pop(0)
        y, x, k, c = golist[0], golist[1], golist[2], golist[3]
        # print(y, x, k, c)
        if four_go == 0:
            y, x, k, c = command(y, x, k, c)
            if [y, x, k, c] not in go_list:
                go_list.append([y, x, k, c])
        if k == -1:
            break
        if flag:
            break
        if four_go :
            # print([y+1, x, k, 1], [y, x+1, k, 2] , [y-1, x, k, 0] , [y, x-1, k, 3] )
            if [y+1, x, k, c] not in go_list:
                if MAP[y+1][x] != 'v':
                    go_list.append([y+1, x, k, 1])
            if [y, x+1, k, c] not in go_list:
                if MAP[y][x+1] != '<':
                    go_list.append([y, x+1, k, 3])
            if [y-1, x, k, c] not in go_list:
                if MAP[y-1][x] != '^':
                    go_list.append([y-1, x, k, 0])
            if [y, x-1, k, c] not in go_list:
                if MAP[y+1][x] != '>':
                    go_list.append([y, x-1, k, 2])
            four_go = 0
    if flag :
        print('#{} YES'.format(tc))
    else :
        print('#{} NO'.format(tc))