T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    tri = [[] for i in range(N + 1)]
    cnt = 0
    for i in range(M):
        x, y = map(int, input().split())
        tri[x].append(y)
        tri[y].append(x)
    for i in range(1, N + 1):
        for j in tri[i]:
            if j < i :
                continue
            else:
                for k in tri[j]:
                    if k < j:
                        continue
                    elif i in tri[k]:
                        cnt += 1
    print('#{} {}'.format(test_case, cnt))