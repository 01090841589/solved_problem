T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    dummy = []
    for A in range(n):
        dummy.append(int(input()))
    cnt = 0
    for aa in range(1000):
        if max(dummy) == min(dummy):
            break
        dummy[dummy.index(max(dummy))] -= 1
        dummy[dummy.index(min(dummy))] += 1
        cnt += 1
    print('#{} {}'.format(test_case,cnt))