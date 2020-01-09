import sys
sys.stdin = open("ACMCraft.txt")

import sys
T = int(sys.stdin.readline())
for tc in range(1, T+1):
    res = 0
    N, K = map(int, sys.stdin.readline().split())
    times = list(map(int, sys.stdin.readline().split()))
    node = [[] for x in range(N+1)]
    visited = [-1] * (N)
    visited2 = [0] * (N)
    for i in range(K):
        bef, aft = map(int, sys.stdin.readline().split())
        node[aft].append(bef)
    target = int(input())
    visited[target-1] = times[target-1]
    que = [[target, times[target-1]]]
    while que:
        num, scr = que.pop()
        visited2[num-1] = 1
        for route in node[num]:
            if visited[route - 1] < scr + times[route - 1] and visited2[route-1] == 0:
                visited[route - 1] = scr + times[route - 1]
                que.append([route, scr+times[route - 1]])
        node[num] = []
    print(max(visited))

    print(visited)