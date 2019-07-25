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
                    cnt = 98
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
                cnt = 99
            break
    return cnt, fail

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    mat = []
    mat_x = []
    for NN in range(N):
        mat_x = list(map(int,input().split()))
        mat.append(mat_x)
    total = 1
    while total > 0:
        total = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                route = []
                fail_route = []
                if mat[i][j] == 1:
                    for k in range(4):
                        rout, fail = length(i,j,k,0)
                        route.append(rout)
                        fail_route.append(fail)
                        if 99 in route:
                            mat[i][j] = 2
                        for fr in range(len(fail_route)):
                            if fail_route[fr] != 9 and route[fr] == min(route) and len(route)==4:
                                if mat[i][j] == 1:
                                    length(i, j, fr, 2)
                                    mat[i][j] = 2
                        if route.count(98)+route.count(99) == 4 and mat[i][j] == 1:
                            mat[i][j] = 4
                if route.count(98)+route.count(99) == 3 and mat[i][j] == 1:
                    for k in range(4):
                        if route[k] != 98 and route[k] != 99:
                            mat[i][j] = 2
                            length(i,j,k,1)
        for i in range(len(mat)):
            total += mat[i].count(1)
        #     print(mat[i])
        # print()
    for i in range(len(mat)):
        # print(mat[i])
        total += mat[i].count(3)
    # print()

    print('#{0} {1}'.format(test_case,total))