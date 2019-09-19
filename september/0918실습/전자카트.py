import sys
sys.stdin = open("전자카트.txt")

def ordered(N, j, gone, cnt, total):
    global result
    if cnt > N:
        return
    if result < total:
        return
    if cnt >= N and sum(gone) == N and j == 0:
        if result > total:
            result = total
        return
    for i in range(N):
        if i == j:
            continue
        if gone[i] == 1:
            continue
        gone[i] = 1
        ordered(N, i, gone, cnt+1, total + mat[j][i])
        gone[i] = 0
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    result =100 * n
    mat = [list(map(int, input().split())) for _ in range(n)]
    ordered(n, 0, [0]*n, 0, 0)

    print("#{} {}".format(test_case, result))