import sys
sys.stdin = open("수열합.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = []
    if M > 500:
        M = 500
    for A in range(M):
        num = list(map(int,input().split()))
        buf = []
        flag = 1
        if len(result) == 0:
            result.extend(num)
        else:
            for i, j in enumerate(result):
                if num[0] < j:
                    result = result[:i] + num + result[i:]
                    flag = 0
                    break
            if len(buf) == 0 and flag:
                result.extend(num)
    print('#{}'.format(tc),end='')
    for i in range(1, 11):
        print(' {}'.format(result[-i]),end='')
    print()