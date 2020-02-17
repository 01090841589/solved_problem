import sys
sys.stdin = open("벌꿀채취.txt")

def dfs(x, sum):
    global cnt, sum2
    visited[x] = 1
    if sum > C:
        return
    sum2 += tmp2[x] ** 2

    if sum2 > cnt:
        cnt = sum2

    for i in range(M):
        if visited[i] == 1:
            continue

        dfs(i, sum + tmp2[i])
        visited[i] = 0
        sum2 -= tmp2[i] ** 2


T = int(input())

for test in range(1, T + 1):
    N, M, C = map(int, input().split())
    nxn = [[0 for _ in range(N)] for _ in range(N)]
    for z in range(N):
        nxn[z] = list(map(int, input().split()))
    arr = []
    for i in range(N):
        for j in range(N):
            br = 0
            for k in range(M):
                if j + k >= N:
                    br = 1
                    break
            if br == 1:
                continue
            tmp = []
            tmp2 = []
            cnt = 0
            for k in range(M):
                tmp.append((i, j + k))
                tmp2.append(nxn[i][j + k])

            for w in range(M):
                visited = [0 for _ in range(M)]
                sum2 = 0
                dfs(w, tmp2[w])

            tmp.insert(0, cnt)
            arr.append(tmp)

    arr.sort(reverse=True)
    L = len(arr)
    ans = []

    for i in range(L - 1):
        for j in range(i + 1, L):
            br = 0
            tmp = arr[i][0] + arr[j][0]
            tmp2 = arr[i][1:]
            for k in range(1, M + 1):
                if arr[j][k] in tmp2:
                    br = 1
                    break
            if br == 1:
                continue
            ans.append(tmp)
    ans.sort(reverse=True)

    print("#%d %d" % (test, ans[0]))