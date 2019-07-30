T = int(input())
for test_case in range(1, T+1):
    NM = list(map(int,input().split()))
    v = list(map(int,input().split()))
    total = []
    for i in range(NM[0]-NM[1]+1):
        add = 0
        for j in range(NM[1]):
            add += v[i+j]
        total.append(add)
    print('#{0} {1}'.format(test_case, max(total)-min(total)))