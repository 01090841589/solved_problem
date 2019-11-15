import sys
sys.stdin = open("디저트카페.txt")

def dessert(y, x, left, right):
    global result, cnt
    if result > (left+result)*2:
        return
    if 0 <= x-left and x+right < N:
        cnt += 1
        Y = y
        X = x
        for i in range(left):
            Y += 1
            X -= 1
            if visited[MAP[Y][X]] != cnt:
                visited[MAP[Y][X]] = cnt
            else:
                return
        for i in range(right):
            Y += 1
            X += 1
            if visited[MAP[Y][X]] != cnt:
                visited[MAP[Y][X]] = cnt
            else:
                return
        for i in range(left):
            Y -= 1
            X += 1
            if visited[MAP[Y][X]] != cnt:
                visited[MAP[Y][X]] = cnt
            else:
                return
        for i in range(right):
            Y -= 1
            X -= 1
            if visited[MAP[Y][X]] != cnt:
                visited[MAP[Y][X]] = cnt
            else:
                return
        if result < visited.count(cnt):
            result = visited.count(cnt)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    hei = N
    result = -1
    cnt = 0
    visited = [0]*101
    for k in range(hei-1, 1, -1):
        for y in range(N-k):
            for x in range(1, N-1):
                if MAP[y][x] > 0 and hei > 1:
                        for l in range(1, k):
                            dessert(y, x, l, k-l)

    print('#{} {}'.format(tc, result))
