
T = int(input())
for test_case in range(1,T+1):
    line = []
    N = []
    M = input().split(' ')
    M = list(map(int,M))
    for a in range(1,M[0]+1):
        N.append(a)
    for a in range(M[1]):
        L = input().split(' ')
        L = list(map(int,L))
        line.append(sorted(L))
        line.sort()
    cal_tri = []
    for check in range(len(N)):
        tri = []
        line_check = []
        for i in range(len(line)):
            if N[check] in line[i]:
                tri.append(line[i])
        for j in range(len(tri)):
            for k in range(j+1, len(tri)):
                line_check = []
                if tri[j][0] == N[check]:
                    line_check.append(tri[j][1])
                else:
                    line_check.append(tri[j][0])
                if tri[k][0] == N[check]:
                    line_check.append(tri[k][1])
                else:
                    line_check.append(tri[k][0])
                if len(line_check) == 2:
                    if sorted(line_check) in line:
                        if sorted([tri[j],tri[k],line_check]) in cal_tri:
                            continue
                        else:
                            cal_tri.append(sorted([tri[j],tri[k],line_check]))
                tri.sort()
    print('#{0} {1}'.format(test_case,len(cal_tri)))