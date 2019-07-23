A = [i for i in range(1,401,2)]
B = [j for j in range(2,402,2)]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    stu = []
    left = 0
    for man in range(N):
        stu.append(list(map(int,input().split())))
    for b in range(len(stu)):
        if stu[b][0] > stu[b][1]:
            stu[b][0], stu[b][1] = stu[b][1], stu[b][0]
    while len(stu) > 0:
        stu.sort()
        way = [1 for k in range(200)]
        for a in range(len(stu)-1, -1, -1):
            cnt = 0
            for i in range(stu[a][0],stu[a][1]+1):
                if way[(i-1) // 2] == 1:
                    cnt += 1
            if cnt == (stu[a][1]-stu[a][0]+1):
                for i in range(stu[a][0], stu[a][1] + 1):
                    way[(i - 1) // 2] = 0
                stu.pop(a)
        left += 1
    print('#{0} {1}'.format(test_case,left))