T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    distance = 0
    velo = 0
    for a in range(N):
        val = input().split(' ')
        if len(val) == 2:
            intersec, ms = int(val[0]), int(val[1])
        elif len(val) == 1:
            intersec = int(val[0])
        if intersec == 0 :
            distance += velo
        elif intersec == 1:
            distance += (velo + ms)
            velo += ms
        else:
            if (velo-ms) < 0 :
                distance += 0
                velo = 0
            else :
                distance += (velo - ms)
                velo -= ms
    print('#{0} {1}'.format(test_case,distance))