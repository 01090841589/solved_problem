import sys
sys.stdin = open("게리멘더링.txt")

import itertools

def bfs(town):
    if len(town) == 1:
        return False
    visited = [0] * N
    queue = [town[0]]
    visited[town[0]] = 1
    while queue:
        a = queue.pop(0)
        for i in range(N):
            if route[a][i] == 1 and visited[i] == 0 and i in town:
                visited[i] = 1
                queue.append(i)
    for a, i in  enumerate(visited):
        if a not in town:
            continue
        if visited[a] == 1 and a in town:
            continue
        else:
            return True
    return False


N = int(input())
people = list(map(int, input().split()))
route = [[0]*N for _ in range(N)]
for i in range(N):
    A = list(map(int, input().split()))
    for j in range(1, len(A)):
        route[i][A[j]-1] = 1

result = 999999
for towns in itertools.permutations(range(N), N):
    for i in range(1, N):
        town1 = list(towns[:i])
        town2 = list(towns[i:])
        if bfs(town1):
            continue
        if bfs(town2):
            continue
        people1 = 0
        for i in town1:
            people1 += people[i]
        people2 = 0
        for i in town2:
            people2 += people[i]

        cnt = abs(people1 - people2)
        if result > cnt:
            result = cnt
    if result == 999999:
        result = -1
print('{}'.format(result))
