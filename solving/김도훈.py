T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    N = list(map(int,input().split()))
    m = int(input())
    M = list(map(int,input().split()))
    N.sort(reverse=True)
    M.sort(reverse=True)
    cnt = 0
    while len(M) > 0:
        success = 0
        for i in N:
            if len(M) == 0:
                break
            if min(M) <= i:
                for a in range(len(M)):
                    if M[a] <= i:
                        del M[a]
                        success += 1
                        break
        if success == 0:
            M = []
            cnt = -1
            break
        cnt+=1
    print('#{0} {1}'.format(test_case,cnt))
