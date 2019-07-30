def makepermu(idx, cnt, make, visit, sum_):
    global arr
    global result
    if sum_ > result:
        return
    if cnt >= idx:
        result = min(result, sum_)
        return
    for i in range(idx):
        if visit[i] == 1:
            continue
        visit[i] = 1
        makepermu(idx, cnt + 1, make, visit, sum_ + arr[cnt][i])
        visit[i] = 0


tc = int(input())
for i in range(1, tc + 1):
    n = int(input())
    arr = [[]] * n
    visit = [0] * n
    make = [0] * n
    result = 1000000
    for j in range(n):
        arr[j] = list(map(int, input().split()))
    makepermu(n, 0, make, visit, 0)

    print("#{} {}".format(i, result))