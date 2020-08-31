import sys
sys.stdin = open("shortest.txt")

from collections import deque

def solve(S):
    queue = deque()
    queue.append(S)
    visited[S - 1] = 1
    while queue:
        v = queue.popleft()
        for n, d in graph[v - 1]:
            if dist[v - 1] + d < dist[n - 1]:
                dist[n - 1] = dist[v - 1] + d
                if not visited[n - 1] or n != G:
                    queue.append(n)
                    visited[n - 1] = 1


T = int(input())
for tc in range(1, T + 1):
    N, M, S, G = map(int, input().split())
    graph = [[] for _ in range(N)]

    for i in range(M):
        u, v, w = map(int, input().split())
        graph[u - 1].append([v, w])
        graph[v - 1].append([u, w])
    dist = [1000000 * M * 2] * N

    visited = [0] * N
    dist[S - 1] = 0
    solve(S)
    print('#%d %d' % (tc, dist[G - 1]))