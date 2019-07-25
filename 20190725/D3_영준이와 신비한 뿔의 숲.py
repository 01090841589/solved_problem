T = int(input())
for test_case in range(1,T+1):
    N = list(map(int,input().split()))
    print('#{0} {1} {2}'.format(test_case,N[0]-((N[0]-N[1])*2),N[0]-N[1]))