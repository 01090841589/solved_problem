import sys
sys.stdin = open('스도쿠.txt')

T = int(input())
for tc in range(1, T+1):
    MAP = [list(map(int, input().split())) for _ in range(9)]
    flag = 0
    xy = [[[] for _ in range(3)] for _ in range(3)]
    for a in range(9):
        xarr, yarr = [], []
        for b in range(9):
            xarr.append(MAP[a][b]) if MAP[a][b] not in xarr else 0
            yarr.append(MAP[b][a]) if MAP[b][a] not in yarr else 0
            xy[a//3][b//3].append(MAP[a][b]) if MAP[a][b] not in xy[a//3][b//3] else 0
        if len(xarr)+len(yarr) != 18:
            flag = 1
    for a in xy:
        for b in a:
            if len(b) != 9:
                flag = 1
    print('#{} {}'.format(tc, (flag+1)%2))