import sys
sys.stdin = open("디저트카페.txt")

def cafe(K, n):
    global total
    if n > 0:
        return
    if K < 2:
        return
    for xsis in range(1, K - 1):
        ysis = (K - 1) - xsis
        for y in range(N):
            for x in range(1, N - 1):
                if route(y, x, ysis, xsis):
                    n = (ysis + xsis) * 2
                    total = n
                    print(y, x, ysis, xsis)
                    break
            if n > 0:
                break
        if n > 0:
            break
    cafe(K - 1, n)


def route(y, x, ysis, xsis):
    global cnt
    if x - ysis < 0 or x + xsis >= N or y + xsis + ysis >= N:
        return False
    else:
        cnt += 1
        for _ in range(ysis):
            y = y + 1
            x = x - 1
            if V[MAP[y][x]] != cnt:
                V[MAP[y][x]] = cnt
            else:
                return False
        for _ in range(xsis):
            y = y + 1
            x = x + 1
            if V[MAP[y][x]] != cnt:
                V[MAP[y][x]] = cnt
            else:
                return False
        for _ in range(ysis):
            y = y - 1
            x = x + 1
            if V[MAP[y][x]] != cnt:
                V[MAP[y][x]] = cnt
            else:
                return False
        for _ in range(xsis):
            y = y - 1
            x = x - 1
            if V[MAP[y][x]] != cnt:
                V[MAP[y][x]] = cnt
            else:
                return False
        return True


V = [0] * 101
cnt = 0
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    total = -1
    cafe(N, 0)
    print('#{} {}'.format(tc, total))
