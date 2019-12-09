import sys
sys.stdin = open('일분배.txt')

def search_num(N, cnt, gone, total):
    global result
    if total <= result:
        return False
    if cnt >= N:
        result = max(result, total)
        return False
    for i in range(N):
        if gone[i] == 1:
            continue
        gone[i] = 1
        search_num(N, cnt + 1, gone, total*(mat[cnt][i]/100))
        gone[i] = 0
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    result = 0
    mat = [list(map(int, input().split())) for _ in range(n)]
    search_num(n, 0, [0]*n, 1)

    print("#%d %0.6f" % (test_case, result*100))