import sys
sys.stdin = open('디저트.txt')

DIR = [[1, -1], [1, 1], [-1, 1], [-1, -1]]


def cafe(K, n):
    global total
    if n > 0:
        return
    if K < 2:
        return
    for xsis in range(1, K-1):
        ysis = (K-1)-xsis
        for y in range(N):
            for x in range(1, N-1):
                if route(y, x, ysis, xsis, n):
                    n = (ysis+xsis)*2
                    total = n
    cafe(K-1, n)


def route(y, x, ysis, xsis, n):
    diss = []
    if x - ysis < 0 or x + xsis >= N or y +xsis+ysis >= N :
        return False
    else:
        for DIR1 in range(ysis):
            y = y+DIR[0][0]
            x = x+DIR[0][1]
            if MAP[y][x] not in diss:
                diss.append(MAP[y][x])
            else: return False
        for DIR2 in range(xsis):
            y = y+DIR[1][0]
            x = x+DIR[1][1]
            if MAP[y][x] not in diss:
                diss.append(MAP[y][x])
            else: return False
        for DIR3 in range(ysis):
            y = y+DIR[2][0]
            x = x+DIR[2][1]
            if MAP[y][x] not in diss:
                diss.append(MAP[y][x])
            else: return False
        for DIR4 in range(xsis):
            y = y+DIR[3][0]
            x = x+DIR[3][1]
            if MAP[y][x] not in diss:
                diss.append(MAP[y][x])
            else: return False
        return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    # [print(MAP[i]) for i in range(N)]
    total = -1

    cafe(N, 0)
    print('#{} {}'.format(tc, total))