T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    n = list(map(int,input().split()))
    print('#{0} {1}'.format(test_case,max(n)-min(n)))