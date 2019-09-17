import sys
sys.stdin = open('2048.txt')


def sum_2048(SUM):
    while True:
        long = len(SUM)
        for i in range(len(SUM)-1):
            if SUM[i] == SUM[i+1] and type(SUM[i]) == int:
                SUM[i] = str(SUM[i]*2)
                del SUM[i+1]
                break
        if long == len(SUM):
            break
    for i in range(N-len(SUM)):
        SUM.append(0)


T = int(input())
for test_case in range(1, T+1):
    N, M = input().split()
    N = int(N)
    mat = [list(map(int, input().split())) for _ in range(N)]
    if M == 'up':
        for x in range(N):
            SUM = []
            for y in range(N):
                if mat[y][x] != 0:
                    SUM.append(mat[y][x])
            sum_2048(SUM)
            for y in range(N):
                mat[y][x] = int(SUM[y])
    elif M == 'down':
        for x in range(N):
            SUM = []
            for y in range(N-1, -1, -1):
                if mat[y][x] != 0:
                    SUM.append(mat[y][x])
            sum_2048(SUM)
            for y in range(N-1, -1, -1):
                mat[N-1-y][x] = int(SUM[y])
    elif M == 'left':
        for y in range(N):
            SUM = []
            for x in range(N):
                if mat[y][x] != 0:
                    SUM.append(mat[y][x])
            sum_2048(SUM)
            for x in range(N):
                mat[y][x] = int(SUM[x])
    elif M == 'right':
        for y in range(N):
            SUM = []
            for x in range(N-1, -1, -1):
                if mat[y][x] != 0:
                    SUM.append(mat[y][x])
            sum_2048(SUM)
            for x in range(N-1, -1, -1):
                mat[y][N-1-x] = int(SUM[x])
    print('#{}'.format(test_case))
    [print(' '.join(list(map(str,mat[i])))) for i in range(N)]