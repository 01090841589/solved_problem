import sys
sys.stdin = open("미생물배양.txt")


DIR = [[-1, 0], [1, 0], [0, -1], [0, 1]]
T = int(input())
for tc in range(1, T+1):
    units = []
    N, M, K = map(int, input().split())
    MAP = [[0] *N for _ in range(N)]
    for k in range(K):
        y, x, scr, c = map(int, input().split())
        MAP[y][x] = [scr, c]
        units.append([y, x, scr, c])
    # print(units)

    for time in range(M):
        units_move = units[:]
        units = []
        for unit in units_move:
            MAP[unit[0]][unit[1]] = 0
        units_move.sort(key=lambda k:k[2])
        for unit in units_move:
            y, x, scr, c = unit
            y = y+DIR[c-1][0]
            x = x+DIR[c-1][1]
            if y == 0 or y == N-1 or x == 0 or x == N-1:
                scr //= 2
                if c % 2 == 0:
                    c -= 1
                else:
                    c += 1
            if MAP[y][x] == 0:
                MAP[y][x] = [scr, c]
            else:
                a = MAP[y][x][0]
                MAP[y][x] = [scr+a, c]
        for yy in range(N):
            for xx in range(N):
                if MAP[yy][xx]:
                    units.append([yy, xx, MAP[yy][xx][0], MAP[yy][xx][1]])
        # print(units)
    result = 0
    for unit in units:
        result += unit[2]
    print("#{} {}".format(tc, result))