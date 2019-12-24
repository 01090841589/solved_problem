import sys
sys.stdin = open("구슬탈출.txt")

DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def turn(ry, rx, by, bx, k):
    global result
    if result <= k:
        return
    for c in DIR:
        if result <= k:
            return
        MAP[ry][rx] = 'R'
        MAP[by][bx] = 'B'
        RY, RX, BY, BX = ry, rx, by, bx
        if c == [0, 1]:
            if bx <= rx:
                while True:
                    MAP[RY][RX] = '.'
                    RY += c[0]
                    RX += c[1]
                    if MAP[RY][RX] == 'O':
                        break
                    elif MAP[RY][RX] == '#':
                        RY -= c[0]
                        RX -= c[1]
                        MAP[RY][RX] = 'R'
                        break
                    else:
                        MAP[RY][RX] = 'R'
                while True:
                    MAP[BY][BX] = '.'
                    BY += c[0]
                    BX += c[1]
                    if MAP[BY][BX] == 'O':
                        break
                    elif MAP[BY][BX] == '#' or MAP[BY][BX] == 'R':
                        BY -= c[0]
                        BX -= c[1]
                        MAP[BY][BX] = 'B'
                        break
                    else:
                        MAP[BY][BX] = 'B'
            else:
                while True:
                    MAP[BY][BX] = '.'
                    BY += c[0]
                    BX += c[1]
                    if MAP[BY][BX] == 'O':
                        break
                    elif MAP[BY][BX] == '#':
                        BY -= c[0]
                        BX -= c[1]
                        MAP[BY][BX] = 'B'
                        break
                    else:
                        MAP[BY][BX] = 'B'
                while True:
                    MAP[RY][RX] = '.'
                    RY += c[0]
                    RX += c[1]
                    if MAP[RY][RX] == 'O':
                        break
                    elif MAP[RY][RX] == '#' or MAP[RY][RX] == 'B':
                        RY -= c[0]
                        RX -= c[1]
                        MAP[RY][RX] = 'R'
                        break
                    else:
                        MAP[RY][RX] = 'R'
            MAP[RY][RX] = '.'
            MAP[BY][BX] = '.'
            MAP[ori[0]][ori[1]] = 'O'
            if MAP[BY][BX] != 'O' and MAP[RY][RX] == 'O':
                if result > k:
                    result = k
            elif BY == by and BX == bx and RY == ry and RX == rx:
                continue
            elif MAP[BY][BX] != 'O' and MAP[RY][RX] != 'O':
                turn(RY, RX, BY, BX, k+1)

        elif c == [0, -1]:
            if bx >= rx:
                while True:
                    MAP[RY][RX] = '.'
                    RY += c[0]
                    RX += c[1]
                    if MAP[RY][RX] == 'O':
                        break
                    elif MAP[RY][RX] == '#':
                        RY -= c[0]
                        RX -= c[1]
                        MAP[RY][RX] = 'R'
                        break
                    else:
                        MAP[RY][RX] = 'R'
                while True:
                    MAP[BY][BX] = '.'
                    BY += c[0]
                    BX += c[1]
                    if MAP[BY][BX] == 'O':
                        break
                    elif MAP[BY][BX] == '#' or MAP[BY][BX] == 'R':
                        BY -= c[0]
                        BX -= c[1]
                        MAP[BY][BX] = 'B'
                        break
                    else:
                        MAP[BY][BX] = 'B'
            else:
                while True:
                    MAP[BY][BX] = '.'
                    BY += c[0]
                    BX += c[1]
                    if MAP[BY][BX] == 'O':
                        break
                    elif MAP[BY][BX] == '#':
                        BY -= c[0]
                        BX -= c[1]
                        MAP[BY][BX] = 'B'
                        break
                    else:
                        MAP[BY][BX] = 'B'
                while True:
                    MAP[RY][RX] = '.'
                    RY += c[0]
                    RX += c[1]
                    if MAP[RY][RX] == 'O':
                        break
                    elif MAP[RY][RX] == '#' or MAP[RY][RX] == 'B':
                        RY -= c[0]
                        RX -= c[1]
                        MAP[RY][RX] = 'R'
                        break
                    else:
                        MAP[RY][RX] = 'R'
            MAP[RY][RX] = '.'
            MAP[BY][BX] = '.'
            MAP[ori[0]][ori[1]] = 'O'
            if MAP[BY][BX] != 'O' and MAP[RY][RX] == 'O':
                if result > k:
                    result = k
            elif BY == by and BX == bx and RY == ry and RX == rx:
                continue
            elif MAP[BY][BX] != 'O' and MAP[RY][RX] != 'O':
                turn(RY, RX, BY, BX, k+1)

        elif c == [1, 0]:
            if by <= ry:
                while True:
                    MAP[RY][RX] = '.'
                    RY += c[0]
                    RX += c[1]
                    if MAP[RY][RX] == 'O':
                        break
                    elif MAP[RY][RX] == '#':
                        RY -= c[0]
                        RX -= c[1]
                        MAP[RY][RX] = 'R'
                        break
                    else:
                        MAP[RY][RX] = 'R'
                while True:
                    MAP[BY][BX] = '.'
                    BY += c[0]
                    BX += c[1]
                    if MAP[BY][BX] == 'O':
                        break
                    elif MAP[BY][BX] == '#' or MAP[BY][BX] == 'R':
                        BY -= c[0]
                        BX -= c[1]
                        MAP[BY][BX] = 'B'
                        break
                    else:
                        MAP[BY][BX] = 'B'
            else:
                while True:
                    MAP[BY][BX] = '.'
                    BY += c[0]
                    BX += c[1]
                    if MAP[BY][BX] == 'O':
                        break
                    elif MAP[BY][BX] == '#':
                        BY -= c[0]
                        BX -= c[1]
                        MAP[BY][BX] = 'B'
                        break
                    else:
                        MAP[BY][BX] = 'B'
                while True:
                    MAP[RY][RX] = '.'
                    RY += c[0]
                    RX += c[1]
                    if MAP[RY][RX] == 'O':
                        break
                    elif MAP[RY][RX] == '#' or MAP[RY][RX] == 'B':
                        RY -= c[0]
                        RX -= c[1]
                        MAP[RY][RX] = 'R'
                        break
                    else:
                        MAP[RY][RX] = 'R'
            MAP[RY][RX] = '.'
            MAP[BY][BX] = '.'
            MAP[ori[0]][ori[1]] = 'O'
            if MAP[BY][BX] != 'O' and MAP[RY][RX] == 'O':
                if result > k:
                    result = k
            elif BY == by and BX == bx and RY == ry and RX == rx:
                continue
            elif MAP[BY][BX] != 'O' and MAP[RY][RX] != 'O':
                turn(RY, RX, BY, BX, k+1)

        elif c == [-1, 0]:
            if by >= ry:
                while True:
                    MAP[RY][RX] = '.'
                    RY += c[0]
                    RX += c[1]
                    if MAP[RY][RX] == 'O':
                        break
                    elif MAP[RY][RX] == '#':
                        RY -= c[0]
                        RX -= c[1]
                        MAP[RY][RX] = 'R'
                        break
                    else:
                        MAP[RY][RX] = 'R'
                while True:
                    MAP[BY][BX] = '.'
                    BY += c[0]
                    BX += c[1]
                    if MAP[BY][BX] == 'O':
                        break
                    elif MAP[BY][BX] == '#' or MAP[BY][BX] == 'R':
                        BY -= c[0]
                        BX -= c[1]
                        MAP[BY][BX] = 'B'
                        break
                    else:
                        MAP[BY][BX] = 'B'
            else:
                while True:
                    MAP[BY][BX] = '.'
                    BY += c[0]
                    BX += c[1]
                    if MAP[BY][BX] == 'O':
                        break
                    elif MAP[BY][BX] == '#':
                        BY -= c[0]
                        BX -= c[1]
                        MAP[BY][BX] = 'B'
                        break
                    else:
                        MAP[BY][BX] = 'B'
                while True:
                    MAP[RY][RX] = '.'
                    RY += c[0]
                    RX += c[1]
                    if MAP[RY][RX] == 'O':
                        break
                    elif MAP[RY][RX] == '#' or MAP[RY][RX] == 'B':
                        RY -= c[0]
                        RX -= c[1]
                        MAP[RY][RX] = 'R'
                        break
                    else:
                        MAP[RY][RX] = 'R'
            MAP[RY][RX] = '.'
            MAP[BY][BX] = '.'
            MAP[ori[0]][ori[1]] = 'O'
            if MAP[BY][BX] != 'O' and MAP[RY][RX] == 'O':
                if result > k:
                    result = k
            elif BY == by and BX == bx and RY == ry and RX == rx:
                continue
            elif MAP[BY][BX] != 'O' and MAP[RY][RX] != 'O':
                turn(RY, RX, BY, BX, k+1)


N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
result = 11
red, blue, ori = [], [], []
for y in range(N):
    for x in range(M):
        if MAP[y][x] == 'R':
            red = [y, x]
        if MAP[y][x] == 'B':
            blue = [y, x]
        if MAP[y][x] == 'O':
            ori = [y, x]

MAP[red[0]][red[1]] = '.'
MAP[blue[0]][blue[1]] = '.'
turn(red[0], red[1], blue[0], blue[1], 1)
if result == 11:
    print(0)
else:
    print(1)