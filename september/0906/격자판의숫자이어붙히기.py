import sys
sys.stdin = open('격자판.txt')
DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def seven(y, x, k, s):
    if k == 0:
        s += MAP[y][x]
    if k == 6:
        result.append(s)
        return
    for c in DIR:
        Y = y+c[0]
        X = x+c[1]
        if 0 <= X < 4 and 0 <= Y < 4:
            seven(Y, X, k+1, s+MAP[Y][X])


T = int(input())
for tc in range(1, T+1):
    MAP = [list(map(str, input().split())) for _ in range(4)]
    result = []
    for y in range(4):
        for x in range(4):
            seven(y, x, 0, '')
    result = set(result)
    print('#{} {}'.format(tc, len(result)))