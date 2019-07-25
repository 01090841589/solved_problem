T = int(input())
for test_case in range(1,T+1):
    NM = list(map(int,input().split()))
    N = input().split()
    M = input().split()
    N = set(N)
    M = set(M)
    total = N & M
    # for i in N:
    #     if i in M:
    #         total += 1
    print('#{0} {1}'.format(test_case,len(total)))
