import sys
sys.stdin = open("bus.txt")
T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().strip().split())
    stop = list(map(int, input().strip().split()))
    locate = 0
    cnt = 0
    stop.append(N)
    stop.insert(0,0)
    print
    for i in range(M+1):
        locate += K
        for j in range(len(stop)-1,-1,-1):
            if locate >= stop[j]:
                locate = stop[j]
                break
        if stop[j] == N:
            print('#{0} {1}'.format(test_case,cnt))
            break
        elif cnt == j:
            if cnt != len(stop):
                print('#{0} 0'.format(test_case))
                break
        else :
            cnt += 1
        if i == M:
            print('#{0} 0'.format(test_case))