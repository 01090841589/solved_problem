import sys
sys.stdin = open('터널속의기차.txt')


T = int(input())
for tc in range(1, T+1):
    N, H = map(int, input().strip().split())
    train = list(map(int, input().split()))
    bulb = list(map(int, input().split()))
    cnt = 0
    off = 0
    if bulb[0] == 0:
        cnt += 1
        bulb[0] = 1
    if bulb[-1] == 0:
        cnt += 1
        bulb[-1] = 1
    i = 1
    while i < N:
        if bulb[i] == 1:
            i += 1
        else:
            if train[i] >= H:
                bulb[i] = 1
                cnt += 1
                i += 1
                off = 0
            else:
                if off+train[i] >= H:
                    bulb[i] = 1
                    cnt += 1
                    i += 1
                    off = 0
                # elif off+train[i] == H:
                #     if bulb[i]-1 == 1:
                #         cnt += 1
                #         off = 0
                #     i += 1


                else:
                    off += train[i]
                    i += 1
    print(bulb)
    print('#{} {}'.format(tc,  cnt))

    T = int(input())
    for tc in range(1, T + 1):
        N, H = map(int, input().split())
        train = list(map(int, input().split()))
        bulb = list(map(int, input().split()))
        ans = 0 if bulb[0] else 1
        off = 0
        for i in range(1, N):
            if bulb[i]:
                off = 0
            else:
                off += train[i]
                if off >= H:
                    ans += 1
                    off = 0
                    bulb[i] = 1
        if N > 1 and not bulb[-1]:
            ans += 1
        print('#%s %s' % (tc, ans))