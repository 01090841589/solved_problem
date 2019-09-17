import sys
sys.stdin = open('프로세서.txt')
DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]




def process(num, n, d):
    global result, nums
    # print(y, x, num, 0)
    if num >= len(chip):
        if nums < n:
            nums, result = n, d
        elif nums == n:
            if result > d:
                result = d
        return
    for c in DIR:
        Y, X = chip[num][0],chip[num][1]
        k = 0
        while True:
            # print(Y, X, k)
            Y += c[0]
            X += c[1]
            if Y < 0 or Y >= N or X < 0 or X >= N:
                MAP[chip[num][0]][chip[num][1]] = 2
                process(num+1, n+1, d+k)
                while True:
                    Y -= c[0]
                    X -= c[1]
                    if MAP[Y][X] == 2:
                        MAP[chip[num][0]][chip[num][1]] = 1
                        break
                    elif MAP[Y][X] == 3:
                        MAP[Y][X] = 0

                break
            elif MAP[Y][X] >= 1:
                while True:
                    Y -= c[0]
                    X -= c[1]
                    if MAP[Y][X] == 1:
                        break
                    elif MAP[Y][X] == 3:
                        MAP[Y][X] = 0
                break
            elif MAP[Y][X] <= 0:
                MAP[Y][X] = 3
                k += 1
        if c == [-1,0]:
            process(num+1, n, d)
            return

T = int(input())
for tc in range(1, 4):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    # [print(MAP[i]) for i in range(N)]
    MAPS = [MAP[i][:] for i in range(N)]
    chip = []7576
    result, nums = 0, 0
    for y in range(N):
        for x in range(N):
            if MAP[y][x] == 1:
                if x == 0 or y == 0 or x == N-1 or y == N-1:
                    MAP[y][x] = 2
                else:
                    chip.append([y, x])
    process(0, 0, 0)
    print('#{} {}'.format(tc, result))

    16937

