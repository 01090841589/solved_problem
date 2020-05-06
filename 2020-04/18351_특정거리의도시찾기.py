import sys
sys.stdin = open("특정거리.txt")

from collections import deque


N, M, K, X = map(int, input().split())
visited = [300001]*(N)
MAP = [[] for _ in range(N)]
res = []
for road in range(M):
    a, b = map(int, input().split())
    MAP[a-1].append(b-1)
q = deque()
q.append(X-1)
visited[X-1] = 0
while q:
    site = q.popleft()
    for go in MAP[site]:
        if visited[site]+1 < visited[go]:
            q.append(go)
            visited[go] = visited[site]+1
            if visited[go] == K:
                res.append(go)
if res:
    res.sort()
    [print(i+1) for i in res]
else:
    print(-1)