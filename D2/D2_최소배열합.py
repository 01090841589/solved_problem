def search_num(N, cnt, gone, total):
    global result
    if total > result:
        return False
    if cnt >= N:
        result = min(result, total)
        return False
    for i in range(N):
        if gone[i] == 1:
            continue
        gone[i] = 1
        search_num(N, cnt + 1, gone, total+mat[cnt][i])
        gone[i] = 0
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    mat = []
    result = 9 * n
    for j in range(n):
        mat.append(list(map(int, input().split())))
    search_num(n, 0, [0]*n, 0)

    print("#{} {}".format(test_case, result))