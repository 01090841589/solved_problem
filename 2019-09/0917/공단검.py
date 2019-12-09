import sys
sys.stdin = open("공단검.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = input().strip().split()
    N = int(N)
    k = len(M)
    lst = list()
    for i in range(1, k+1):
        for j in range((q+1)-i):
            lst.append(M[j:j+i])
    lst = list(set(lst))
    lst.sort()
    print('#{} {} {}'.format(tc, lst[N-1][0], len(lst[N-1])))