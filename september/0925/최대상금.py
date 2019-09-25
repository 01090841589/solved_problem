import sys
sys.stdin = open("최대상금.txt")

def permu(k, n, leng):
    global result
    if k == n:
        if result < int(''.join(N)):
            result = int(''.join(N))
        return
    for i in range(leng-1):
        for j in range(i+1, leng):
            N[i], N[j] = N[j], N[i]
            permu(k+1, n, leng)
            N[i], N[j] = N[j], N[i]



T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    N = list(N)
    M = int(M)
    result = 0
    while M > len(N)-1:
        M -= 2
    permu(0, M, len(N))
    print('#{} {}'.format(tc, result))