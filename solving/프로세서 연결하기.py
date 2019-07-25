location = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def length(y, x, i, c):
    cnt = 0
    fail = 0
    while True:
        y = y + location[i][0]
        x = x + location[i][1]
        if 0 <= y < N and 0 <= x < N:
            if c == 0:
                if mat[y][x] == 0:  # 입력 C 와 다르게
                    cnt += 1
                    for connec in range(len(mat)):
                        if location[i][1] != 0:
                            if mat[connec][x] == 1:
                                fail = 9
                        elif location[i][0] != 0:
                            if mat[y][connec] == 1:
                                fail = 9
                else:
                    cnt = 0
                    fail = 9
                    break
            elif c == 1:
                if mat[y][x] == 0:
                    mat[y][x] = 3
            elif c == 2:
                mat[y][x] = 3
        else:
            if cnt == 0:
                fail = 9
                cnt = 'x'
            break
    return cnt, fail



mat = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
mat2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]]
N = len(mat)
print(len(mat))
for i in range(len(mat)):
    print(mat[i])

for i in range(len(mat)):
    for j in range(len(mat)):
        route = []
        if mat[i][j] == 1:
            for k in range(4):
                rout, fail = length(i,j,k,0)
                route.append(rout)
                if fail != 9:
                    if mat[i][j] == 1:
                        length(i, j, k, 2)
                        mat[i][j] = 2
            if 'x' in route:
                mat[i][j] = 2
            print(i,j,route)
        if route.count(0)+route.count('x') == 3 and mat[i][j] == 1:
            for k in range(4):
                if route[k] != 0 and route[k] != 'x':
                    mat[i][j] = 2
                    length(i,j,k,1)
for i in range(len(mat)):
    print(mat[i])