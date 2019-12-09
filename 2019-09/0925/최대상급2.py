import sys
sys.stdin = open("최대상금.txt")


def sev(N, a):
    global result
    nums = list(str(N))
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if a > 0:
                if N not in visited or a <= 4:
                    change(i, j, a, N)

    if a == 0:
        if N not in visited:
            visited.append(N)
        if result < int(N):
            result = int(N)
        return


def change(i, j, a, N):
    N = list(str(N))
    N[i], N[j] = N[j], N[i]
    sev(''.join(N), a - 1)


T = int(input())
for tc in range(1, 11):
    result = 0
    visited = []
    N, K = map(int, input().split())
    sev(N, K)
    print('#{} {}'.format(tc, result))
