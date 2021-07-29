import sys
sys.stdin = open("모노.txt")

total_cascade = 0
num = int(input())
orders = [list(map(int, input().split())) for _ in range(num)]

MAP1 = [[0] * 4 for _ in range(6)]
MAP2 = [[0] * 4 for _ in range(6)]
for order_num, order in enumerate(orders):
    # MAP1
    y, x = order[1], order[2]
    flag = 1
    if order[0] == 1:
        for y_in in range(5, -1, -1):
            if MAP1[y_in][x] != 0:
                flag = 0
                MAP1[y_in + 1][x] = 1
                break
        if flag:
            MAP1[0][x] = 1
    elif order[0] == 2:
        for y_in in range(5, -1, -1):
            if MAP1[y_in][x] != 0 or MAP1[y_in][x + 1] != 0:
                flag = 0
                MAP1[y_in + 1][x], MAP1[y_in + 1][x + 1] = 2, 2
                break
        if flag:
            MAP1[0][x], MAP1[0][x + 1] = 2, 2
    elif order[0] == 3:
        for y_in in range(5, -1, -1):
            if MAP1[y_in][x] != 0:
                flag = 0
                MAP1[y_in + 1][x] = 1
                MAP1[y_in + 2][x] = 1
                break
        if flag:
            MAP1[0][x] = 1
            MAP1[1][x] = 1

    # MAP2
    x, y = order[1], order[2]
    flag = 1
    if order[0] == 1:
        for y_in in range(5, -1, -1):
            if MAP2[y_in][x] != 0:
                flag = 0
                MAP2[y_in + 1][x] = 1
                break
        if flag:
            MAP2[0][x] = 1
    elif order[0] == 2:
        for y_in in range(5, -1, -1):
            if MAP2[y_in][x] != 0:
                flag = 0
                MAP2[y_in + 1][x] = 1
                MAP2[y_in + 2][x] = 1
                break
        if flag:
            MAP2[0][x] = 1
            MAP2[1][x] = 1
    elif order[0] == 3:
        for y_in in range(5, -1, -1):
            if MAP2[y_in][x] != 0 or MAP2[y_in][x + 1] != 0:
                flag = 0
                MAP2[y_in + 1][x], MAP2[y_in + 1][x + 1] = 2, 2
                break
        if flag:
            MAP2[0][x], MAP2[0][x + 1] = 2, 2

    # cascade
    line_out1, line_out2 = [], []
    min_out1, min_out2 = -1, -1
    change_flag = 1
    while change_flag:
        change_flag = 0

        for y_cas in range(5):
            cnt1, cnt2 = 0, 0
            for x_cas in range(4):
                if not MAP1[y_cas][x_cas]:
                    cnt1 += 1
                if not MAP2[y_cas][x_cas]:
                    cnt2 += 1
            if not cnt1:
                line_out1.append(y_cas)
                change_flag = 1
            if not cnt2:
                line_out2.append(y_cas)
                change_flag = 1
        if line_out1:
            min_out1 = line_out1[0]
            while line_out1:
                line_num = line_out1.pop()
                del MAP1[line_num]
                total_cascade += 1
                MAP1.append([0] * 4)

            if min_out1 > 0:
                for y_cas in range(min_out1, 6):
                    for x_cas in range(4):
                        if MAP1[y_cas][x_cas] == 1:
                            for y_down in range(y_cas - 1, -1, -1):
                                if not MAP1[y_down][x_cas]:
                                    MAP1[y_down][x_cas], MAP1[y_cas][x_cas] = MAP1[y_cas][x_cas], MAP1[y_down][x_cas]
                                else:
                                    break
                        elif MAP1[y_cas][x_cas] == 2:
                            if x_cas - 1 >= 0:
                                if MAP1[y_cas][x_cas - 1] == 2:
                                    for y_down in range(y_cas-1, -1, -1):
                                        if not MAP1[y_down][x_cas] and not MAP1[y_down][x_cas - 1]:
                                            MAP1[y_down][x_cas] = MAP1[y_cas][x_cas]
                                            MAP1[y_cas][x_cas] = MAP1[y_down][x_cas]
                                            MAP1[y_down][x_cas - 1] = MAP1[y_cas][x_cas - 1]
                                            MAP1[y_cas][x_cas - 1] = MAP1[y_down][x_cas - 1]
                                        else:
                                            break
                            if x_cas + 1 < 4:
                                if MAP1[y_cas][x_cas + 1] == 2:
                                    for y_down in range(y_cas-1, -1, -1):
                                        if not MAP1[y_down][x_cas] and not MAP1[y_down][x_cas + 1]:
                                            MAP1[y_down][x_cas], MAP1[y_cas][x_cas] = MAP1[y_cas][x_cas], MAP1[y_down][
                                                x_cas]
                                            MAP1[y_down][x_cas + 1] = MAP1[y_cas][x_cas + 1]
                                            MAP1[y_cas][x_cas + 1] = MAP1[y_down][x_cas + 1]
                                        else:
                                            break

        if line_out2:
            min_out2 = line_out2[0]
            while line_out2:
                line_num = line_out2.pop()
                del MAP2[line_num]
                total_cascade += 1
                MAP2.append([0] * 4)
            if min_out2 > 0:
                for y_cas in range(min_out2, 6):
                    for x_cas in range(4):
                        if MAP2[y_cas][x_cas] == 1:
                            for y_down in range(y_cas - 1, -1, -1):
                                if not MAP2[y_down][x_cas]:
                                    MAP2[y_down][x_cas], MAP2[y_cas][x_cas] = MAP2[y_cas][x_cas], MAP2[y_down][x_cas]
                                else:
                                    break
                        elif MAP2[y_cas][x_cas] == 2:
                            if x_cas - 1 >= 0:
                                if MAP2[y_cas][x_cas - 1] == 2:
                                    for y_down in range(y_cas - 1, -1, -1):
                                        if not MAP2[y_down][x_cas] and not MAP2[y_down][x_cas - 1]:
                                            MAP2[y_down][x_cas], MAP2[y_cas][x_cas] = MAP2[y_cas][x_cas], MAP2[y_down][
                                                x_cas]
                                            MAP2[y_down][x_cas - 1], MAP2[y_cas][x_cas - 1] = MAP2[y_cas][x_cas - 1], \
                                                                                              MAP2[y_down][x_cas - 1]
                                        else:
                                            break
                            if x_cas + 1 < 4:
                                if MAP2[y_cas][x_cas + 1] == 2:
                                    for y_down in range(y_cas - 1, -1, -1):
                                        if not MAP2[y_down][x_cas] and not MAP2[y_down][x_cas + 1]:
                                            MAP2[y_down][x_cas], MAP2[y_cas][x_cas] = MAP2[y_cas][x_cas], MAP2[y_down][
                                                x_cas]
                                            MAP2[y_down][x_cas + 1], MAP2[y_cas][x_cas + 1] = MAP2[y_cas][x_cas + 1], \
                                                                                              MAP2[y_down][x_cas + 1]
                                        else:
                                            break

    # overflow
    over1, over2 = 0, 0
    for y_cas in range(4, 6):
        cnt1, cnt2 = 0, 0
        for x_cas in range(4):
            if MAP1[y_cas][x_cas]:
                cnt1 += 1
            if MAP2[y_cas][x_cas]:
                cnt2 += 1
        if cnt1:
            over1 += 1
        if cnt2:
            over2 += 1
    for line_del in range(over1):
        del MAP1[0]
        MAP1.append([0] * 4)
    for line_del in range(over2):
        del MAP2[0]
        MAP2.append([0] * 4)

    for i in range(5, -1, -1):
        print(MAP1[i], MAP2[i])
    print()

scr = 0
for y in range(4):
    for x in range(4):
        if MAP1[y][x]:
            scr += 1
        if MAP2[y][x]:
            scr += 1
print(total_cascade)
print(scr)

