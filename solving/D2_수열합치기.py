T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    result = []
    for A in range(M):
        num = list(map(int,input().split()))
        buf = []
        if len(result) == 0:
            result.extend(num)
        else:
            for i, j in enumerate(result):
                if num[0] < j:
                    buf = result[0:i] + num + result[i:]
                    break
            if len(buf) == 0:
                result.extend(num)
            else:
                result = buf
    print('#{}'.format(test_case),end='')
    for i in range(len(result)-1,len(result)-11,-1):
        print(' {}'.format(result[i]),end='')
    print()