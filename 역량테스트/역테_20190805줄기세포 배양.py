DIR = [[-1, 0], [0, 1], [1, 0], [0, -1]]
def new_up():
    mat.insert(0, [0]*len(mat[0]))
def new_down():
    mat.append([0]*len(mat[0]))
def new_left():
    for ins in range(len(mat)):
        mat[ins].insert(0, 0)
def new_right():
    for ins in range(len(mat)):
        mat[ins].append(0)
def multiple(y, x, c):
    for arr in range(4):
        Y = y+DIR[arr][0]
        X = x+DIR[arr][1]
        if mat[Y][X] == 0:
            mat[Y][X] = c+10
def spread():
    up, down, left, right = 0, 0, 0, 0
    for Ai in range(len(mat)):
        for Aj in range(len(mat[0])):
            if mat[Ai][Aj] != 0:
                if Ai == 0:
                    up = 1
                if Aj == 0:
                    left = 1
                if Ai == len(mat)-1:
                    down = 1
                if Aj == len(mat[0])-1:
                    right = 1
    if up == 1:
        new_up()
    if left == 1:
        new_left()
    if down == 1:
        new_down()
    if right == 1:
        new_right()

T = int(input())
for test_case in range(1, T+1):
    NMK = list(map(int,input().split()))
    mat = []
    for mats in range(NMK[0]):
        mat.append(list(map(int,input().split())))
    for turn in range(1, NMK[2]+1):
        spread()
        for AA in range(10,0,-1):
            if turn % (AA+1) == 0:
                for i in range(len(mat)):
                    for j in range(len(mat[0])):
                        if mat[i][j] == AA:
                            multiple(i, j, AA)
                            mat[i][j] = -AA-1
                for i in range(len(mat)):
                    for j in range(len(mat[0])):
                        if mat[i][j] > 10:
                            mat[i][j] -= 10
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] < -1:
                    mat[i][j] += 1
        cnt = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] > 0:
                    cnt += 1
                elif mat[i][j] < -1:
                    cnt += 1
    print('#{0} {1}'.format(test_case,cnt))