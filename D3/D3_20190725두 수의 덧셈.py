T = int(input())
for test_case in range(1,T+1):
    N = list(map(int,input().split()))
    total = sum(N)
    print('#{0} {1}'.format(test_case,total))