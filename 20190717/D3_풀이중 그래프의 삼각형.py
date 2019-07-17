T = 1
N , M = 5, 10
N = [1, 2, 3, 4, 5]
line = [[1, 2], [1, 3], [2, 3], [1, 4], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5], [4, 5]]
cal_tri = []
for check in range(len(N)):
    tri = []
    line_check = []
    for i in range(len(line)):
        if N[check] in line[i]:
            tri.append(line[i])
    if len(tri) == 2:
        for i in range(len(line)):
            if N[check] in line[i]:
                if line[i][0] == N[check]:
                    line_check.append(line[i][1])
                else:
                    line_check.append(line[i][0])
        if len(line_check) == 2:
            line_check.sort()
            for dot in line:
                if line_check == dot:
                    tri.append(dot)
    tri.sort()
    if len(cal_tri) == 0:
        cal_tri.append((tri))
    else :
        com = 0
        for A in cal_tri:
            if A == tri:
                break
            else :
                com += 1
        if com == len(cal_tri):
            cal_tri.append((tri))

    print(line_check)
    print(tri)
    print(cal_tri)