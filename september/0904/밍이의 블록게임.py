import sys
sys.stdin = open('블록게임.txt')
DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def colors(y, x, a, blocks):
    global max_color, k
    for c in DIR:
        Y = y+c[0]
        X = x+c[1]
        if 0 <= X < M and 0 <= Y < N and MAP[y][x] == MAP[Y][X] and visited[Y][X] == 0:
            visited[Y][X] = a
            k += 1
            colors(Y, X, a, blocks)
    if max_color < k:
        max_color = k
        blocks = []
        blocks.append([y, x, k, a])
    elif max_color == k:
        blocks.append([y, x, k, a])



T = int(input())
for tc in range(1, T+1):
    N, M, Q = map(int, input().split())
    MAP = [list(input()) for _ in range(N)]
    command = []
    for i in range(Q):
        K = input()
        if K[0] == 'U':
            command.append(['U', K[2:]])
        else:
            command.append(K)
    for coms in command:
        if coms[0] == 'U':
            flag = 0
            for x in range(M):
                if MAP[0][x] != '#':
                    flag = 1
                    break
            if flag == 0:
                del MAP[0]
                MAP.append(list(coms[1]))
                for x in range(M):
                    for y in range(N-1, 0, -1):
                        if MAP[y][x] == '#':
                            for Y in range(y-1, -1, -1):
                                if MAP[Y][x] != '#':
                                    MAP[y][x], MAP[Y][x] = MAP[Y][x], MAP[y][x]
                                    break
        elif coms[0] == 'L':
            for y in range(N):
                for x in range(M-1):
                    if MAP[y][x] == '#':
                        for X in range(x+1, M):
                            if MAP[y][X] != '#':
                                MAP[y][x], MAP[y][X] = MAP[y][X], MAP[y][x]
                                break
            for x in range(M):
                for y in range(N - 1, 0, -1):
                    if MAP[y][x] == '#':
                        for Y in range(y - 1, -1, -1):
                            if MAP[Y][x] != '#':
                                MAP[y][x], MAP[Y][x] = MAP[Y][x], MAP[y][x]
                                break
        elif coms[0] == 'R':
            for y in range(N):
                for x in range(M-1, 0, -1):
                    if MAP[y][x] == '#':
                        for X in range(x-1, -1, -1):
                            if MAP[y][X] != '#':
                                MAP[y][x], MAP[y][X] = MAP[y][X], MAP[y][x]
                                break
            for x in range(M):
                for y in range(N - 1, 0, -1):
                    if MAP[y][x] == '#':
                        for Y in range(y - 1, -1, -1):
                            if MAP[Y][x] != '#':
                                MAP[y][x], MAP[Y][x] = MAP[Y][x], MAP[y][x]
                                break
        elif coms[0] == 'D':
            max_color = 0
            visited = [[0]*M for _ in range(N)]
            a = 1
            blocks = []
            for y in range(N):
                for x in range(M):
                    if 0 <= x < M and 0 <= y < N and MAP[y][x] != '#' and visited[y][x] == 0:
                        k = 1
                        visited[y][x] = a
                        blocks.append([y, x, k, a])
                        colors(y, x, a, blocks)
                        a += 1
            for d in blocks:
                if d[2] == max_color:
                    for y in range(N):
                        for x in range(M):
                            if visited[y][x] == d[3]:
                                MAP[y][x] = '#'
            for x in range(M):
                for y in range(N-1, 0, -1):
                    if MAP[y][x] == '#':
                        for Y in range(y-1, -1, -1):
                            if MAP[Y][x] != '#':
                                MAP[y][x], MAP[Y][x] = MAP[Y][x], MAP[y][x]
                                break

    print('#{}'.format(tc))
    [print(''.join(MAP[i])) for i in range(N)]
    print()
