import sys
sys.stdin = open("SmallworldNetwork.txt")

from collections import deque

N, K = map(int, input().split())
MAP = [[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    fir, sec = map(int, input().split())
    MAP[fir][sec] = 1
    MAP[sec][fir] = 1

res = 0
for num in range(1, N+1):
    if res:
        break
    visited = [0]*(N+1)
    visited[num] = 1
    queue = deque([num])
    while queue:
        now = queue.popleft()
        for i in range(1, N+1):
            if MAP[now][i] and visited[i] == 0:
                visited[i] = visited[now]+1
                queue.append(i)
    for i in range(1, N+1):
        if visited[i] == 0 or visited[i] > 7:
            res = 1
            break
if res:
    print("Big World!")
else:
    print("Small World!")