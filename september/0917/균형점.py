from decimal import Decimal

import sys
sys.stdin = open("균형점.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = list(map(int, input().split()))
    mat = M[:N]
    H = M[N:]
    result = []
    for k in range(N-1):
        left = mat[k]
        right = mat[k+1]
        d = (left+right)/2
        total = 1
        while right - left > Decimal(10) ** -12:
            total = 0
            for i in range(N):
                if d < mat[i]:
                    total += H[i]/((d-mat[i]) * (d-mat[i]))
                elif d > mat[i]:
                    total -= H[i] / ((d - mat[i]) * (d - mat[i]))
            if total > 0:
                right = d
                d = (left+d)/2
            elif total < 0:
                left = d
                d = (right+d)/2
            else:
                break
        result.append(d)
    print('#{}'.format(tc), end = ' ')
    for i in range(len(result)):
        print('%.10f' %(result[i]),end=' ')
    print()