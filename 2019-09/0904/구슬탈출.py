import sys
sys.stdin = open('구슬탈출.txt')
DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def turn(ry, rx, by, bx, k):
    global result
    if ry == red[0] and rx == red[1] and by == blue[0] and bx == blue[1] and k >1:
        return
    if result <= k:
        return
    for c in DIR:
        MAP[ry][rx], MAP[by][bx] = 'R', 'B'
        RY, RX = ry, rx
        BY, BX = by, bx
        if RX - BX * sum(c) > 0:
            while True:
                RY += c[0]
                RX += c[1]
                if MAP[RY][RX] == '.':
                    MAP[RY][RX] = 'R'
                    MAP[RY-c[0]][RX-c[1]] = '.'
                    continue
                elif MAP[RY][RX] == 'O':
                    MAP[RY-c[0]][RX-c[1]] = '.'
                    MAP[BY][BX] = '.'
                    if result > k:
                        result = k
                    break
                else:
                    RY -= c[0]
                    RX -= c[1]
                    break
        while True:
            BY += c[0]
            BX += c[1]
            if MAP[BY][BX] == '.':
                MAP[BY][BX] = 'B'
                MAP[BY-c[0]][BX-c[1]] = '.'
                continue
            elif MAP[BY][BX] == 'O':
                MAP[BY-c[0]][BX-c[1]] = '.'
                MAP[RY][RX] = '.'
                result = 11
                break
            else:
                BY -= c[0]
                BX -= c[1]
                break
        if RX - BX * sum(c) <= 0:
            while True:
                RY += c[0]
                RX += c[1]
                if MAP[RY][RX] == '.':
                    MAP[RY][RX] = 'R'
                    MAP[RY-c[0]][RX-c[1]] = '.'
                    continue
                elif MAP[RY][RX] == 'O':
                    MAP[RY-c[0]][RX-c[1]] = '.'
                    MAP[BY][BX] = '.'
                    if result > k:
                        result = k
                    break
                else:
                    RY -= c[0]
                    RX -= c[1]
                    break
        if RY == ry and RX == rx and BY == by and BX == bx:
            MAP[RY][RX], MAP[BY][BX] = '.', '.'
            continue
        else:
            MAP[RY][RX], MAP[BY][BX] = '.', '.'
            if [RY, RX, BY, BX] not in visited:
                visited.append([RY, RX, BY, BX])
                turn(RY, RX, BY, BX, k+1)

N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
result = 11
red, blue = [], []
for y in range(N):
    for x in range(M):
        if MAP[y][x] == 'R':
            red = [y, x]
        if MAP[y][x] == 'B':
            blue = [y, x]
visited = [red[0], red[1], blue[0], blue[1]]


turn(red[0], red[1], blue[0], blue[1], 1)
if result == 11:
    print(0)
else:
    print(1)