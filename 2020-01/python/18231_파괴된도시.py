import sys
sys.stdin = open("파괴된도시.txt")

N, M = map(int, input().split())


MAP = [[] for __ in range(N+1)]
for i in range(M):
    town1, town2 = map(int, input().split())
    MAP[town1].append(town2)
    MAP[town2].append(town1)
K = int(input())
towns = list(map(int, input().split()))
visited = [0] * (N+1)
for i in range(K):
    visited[towns[i]] = 1
result = []
for i in range(K):
    flag = 1
    for j in MAP[towns[i]]:
        if visited[j] == 0:
            flag = 0
            break
    if flag:
        visited[towns[i]] = 2
        for j in MAP[towns[i]]:
            visited[j] = 2
        result.append(towns[i])
flag = 1
for i in range(1, N+1):
    if visited[i] == 1:
        flag = 0
        break

if flag:
    print(len(result))
    result.sort()
    print(' '.join(list(map(str, result))))
    print()
else:
    print(-1)
