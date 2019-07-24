    T = int(input())
    for test_case in range(1, T+1):
        NN = int(input())
        N = list(map(int,input().split()))
        N.sort()
        N1 = []
        N2 = []
        for i in range(len(N)):
            if i % 2 :
                N2.append(N[i])
            else :
                N1.append(N[i])
        N2.sort(reverse=True)
        N1 += N2
        jump = 0
        for i in range(len(N1)):
            if abs(N1[i]-N1[i-1]) > jump:
                jump = abs(N1[i]-N1[i-1])
        print('#{0} {1}'.format(test_case,jump))