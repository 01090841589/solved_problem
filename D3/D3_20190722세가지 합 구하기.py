T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    S1 = N*(N+1)//2
    print('#{0} {1} {2} {3}'.format(test_case,S1,S1*2-N,S1*2))