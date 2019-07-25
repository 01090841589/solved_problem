T = int(input())
for test_case in range(1, T+1):
    N = list(map(int,input()))
    total = -1
    value = N[0]
    while len(N) > 0:\
        if total == 0:
            if value == 1:
                total += 1
        total += 1
        while N[0] == value:
            del N[0]
            if len(N) == 0:
                break
        if len(N) == 0:
            break
        value = N[0]
    print('#{0} {1}'.format(test_case,total))