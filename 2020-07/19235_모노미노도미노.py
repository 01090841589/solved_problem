N = int(input())
def block_cascade(yc, MAPP):
    for _ in range(3):
        for xx in range(4):
            remain = []
            for ycc in range(yc, 6):
                if MAPP[ycc][xx]:
                    remain.append(1)
            if remain == []:
                continue

            remain += [0, 0, 0, 0, 0, 0]
            flag = 1
            for ycc in range(yc - 1, -1, -1):
                if MAPP[ycc][xx] == 1:
                    flag = 0
                    num = ycc
                    for yccc in range(ycc+1, 6):
                        MAPP[yccc][xx] = remain[num]
                        num += 1
            if flag == 1 :
                for yccc in range(6):
                    MAPP[yccc][xx] = remain[yccc]


BLOCK = [[0]*4 for _ in range(4)]
MAP1 = [[0]*4 for _ in range(6)]
MAP2 = [[0]*4 for _ in range(6)]

res = 0
ORDER = [list(map(int, input().split())) for _ in range(N)]
for order in ORDER:
    t, y, x, = order
    if t == 1:
        flag = 1
        for yl in range(5, -1, -1):
            if MAP1[yl][x] == 1:
                flag = 0
                MAP1[yl+1][x] = 1
                break
        if flag:
            MAP1[0][x] = 1
    elif t == 2:
        flag = 1
        for yl in range(5, -1, -1):
            if MAP1[yl][x] == 1 or MAP1[yl][x+1] == 1:
                flag = 0
                MAP1[yl+1][x] = 1
                MAP1[yl+1][x+1] = 1
                break
        if flag:
            MAP1[0][x] = 1
            MAP1[0][x+1] = 1
    elif t == 3:
        flag = 1
        for yl in range(4, -1, -1):
            if MAP1[yl][x] == 1:
                flag = 0
                MAP1[yl+1][x] = 1
                MAP1[yl+2][x] = 1
                break
        if flag:
            MAP1[0][x] = 1
            MAP1[1][x] = 1
    y, x = x, y

    if t == 1:
        flag = 1
        for yl in range(5, -1, -1):
            if MAP2[yl][x] == 1:
                flag = 0
                MAP2[yl+1][x] = 1
                break
        if flag:
            MAP2[0][x] = 1
    elif t == 3:
        flag = 1
        for yl in range(5, -1, -1):
            if MAP2[yl][x] == 1 or MAP2[yl][x+1] == 1:
                flag = 0
                MAP2[yl+1][x] = 1
                MAP2[yl+1][x+1] = 1
                break
        if flag:
            MAP2[0][x] = 1
            MAP2[0][x+1] = 1
    elif t == 2:
        flag = 1
        for yl in range(4, -1, -1):
            if MAP2[yl][x] == 1:
                flag = 0
                MAP2[yl+1][x] = 1
                MAP2[yl+2][x] = 1
                break
        if flag:
            MAP2[0][x] = 1
            MAP2[1][x] = 1


    # while True:
    for yc in range(5, -1, -1):
        if MAP1[yc] == [1, 1, 1, 1]:
            del MAP1[yc]
            MAP1.append([0, 0, 0, 0])
            block_cascade(yc, MAP1)


            res += 1
        if MAP2[yc] == [1, 1, 1, 1]:
            del MAP2[yc]
            MAP2.append([0, 0, 0, 0])
            block_cascade(yc, MAP2)
            res += 1

    MAP1_del = []
    MAP2_del = []

    for yc in range(5, 3, -1):
        for xc in range(4):
            if MAP1[yc][xc]:
                del MAP1[0]
                MAP1.insert(yc, [0,0,0,0])
                break

    for yc in range(5, 3, -1):
        for xc in range(4):
            if MAP2[yc][xc]:
                del MAP2[0]
                MAP2.insert(yc, [0,0,0,0])
                break



    # [print(MAP1[i], MAP2[i]) for i in range(5, -1, -1)]
    # print()




scr = 0
for yy in range(6):
    for xx in range(4):
        if MAP1[yy][xx]:
            scr += 1
        if MAP2[yy][xx]:
            scr += 1
print(res)
print(scr)