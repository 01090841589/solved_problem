import sys
sys.stdin = open("외판원.txt")

def ordered(N, j, gone, cnt, total):
    global result
    if cnt > N:
        return
    if result <= total:
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
        if mat[j][i] > 0:
            ordered(N, i, gone, cnt+1, total + mat[j][i])
        gone[i] = 0
n = int(input())
result = 9999999999
mat = [list(map(int, input().split())) for _ in range(n)]
ordered(n, 0, [0]*n, 0, 0)

print(result)