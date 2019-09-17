import sys
sys.stdin = open('행렬찾기.txt')
DIR = [[0, 1], [1, 0]]

def mat_search(y, x):
    ysis , xsis = 0, 0
    for i in range(1,N):
        Y = y+i
        if Y < N and MAP[Y][x] != 0:
            visited[Y][x] = 1
            continue
        else:
            ysis = Y-1
            break
    for i in range(1,N):
        X = x+i
        if X < N and MAP[y][X] != 0:
            visited[y][X] = 1
            continue
        else:
            xsis = X-1
            break
    for i in range(y, ysis+1):
        for j in range(x, xsis+1):
            visited[i][j] = 1
    return [ysis, xsis]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    size = []
    matrix = []

    for y in range(N):
        for x in range(N):
            if MAP[y][x] != 0 and visited[y][x] == 0:
                visited[y][x] = 1
                [Y, X] = mat_search(y, x)
                if matrix == []:
                    matrix.append([Y-y+1, X-x+1])
                    size.append((Y-y+1) * (X-x+1))
                else:
                    for i in range(len(matrix)):
                        if (Y-y+1) * (X-x+1) < size[i]:
                            size.insert(i, (Y-y+1) * (X-x+1))
                            matrix.insert(i, [Y-y+1, X-x+1])
                            break
                        if (Y-y+1) * (X-x+1) == size[i]:
                            if (Y-y+1) < size[i]:
                                size.insert(i, (Y-y+1) * (X-x+1))
                                matrix.insert(i, [Y-y+1, X-x+1])
                                break
                        if i == len(matrix)-1:
                            matrix.append([Y-y+1, X-x+1])
                            size.append((Y-y+1) * (X-x+1))
    print('#{} {}'.format(tc, len(matrix)),end=' ')
    for a in matrix:
        print(a[0], a[1],end = ' ')
    print()