import sys
sys.stdin = open('미로.txt')

DIR = [[0, 1], [0, -1], [1, 0]]

def mage(y, k, c, scr):
    global rst, rex
    if scr >= rst:
        return
    if y == 0:
        if rst > scr:
            rst = scr
            rex = X[k]
        return
    if 0 <= X[k]+1 < 100 and MAP[y][X[k]+1] == 1 and c == 0:
        mage(y, k+1, 1, scr+X[k+1]-X[k])
    elif 0 <= X[k]-1 < 100 and MAP[y][X[k]-1] == 1 and c == 0:
        mage(y, k-1, 1, scr+X[k]-X[k-1])
    else:
        mage(y-1, k, 0, scr+1)


for tc in range(1, 11):
    rst = 1000
    rex = 0
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(100)]
    X = []
    for x in range(100):
        if MAP[99][x] == 1:
            X.append(x)
    for i in range(len(X)):
        mage(99, i, 0, 0)
    print('#{} {}'.format(tc, rex))