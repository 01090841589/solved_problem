import sys
sys.stdin = open('양팔저울.txt')

def kgs(n, k, lw, rw, ld, rd):
    global cnt
    if lw < rw:
        return 0
    if n == k:
        return 1
    elif d[ld][rd] != -1:
        return d[ld][rd]
    else:
        sum = 0
        for i in range(k):
            if visited[i] == 0:
                visited[i] = 1
                p[n] = i
                sum += kgs(n + 1, k, lw + w[i], rw, ld + (1 << i), rd)
                sum += kgs(n + 1, k, lw, rw + w[i], ld, rd + (1 << i))
                visited[i] = 0
        d[ld][rd] = sum
        return sum


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    w = list(map(int, input().split()))
    rs = sum(w)
    p = [0] * N
    visited = [0] * N

    d = [[-1] * (2 ** (N + 1)) for i in range(2 ** (N + 1))]
    cnt = kgs(0, N, 0, 0, 0, 0)
    print('#{} {}'.format(tc, cnt))