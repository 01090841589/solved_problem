import sys
sys.stdin = open("줄세우기.txt")

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [[] for _ in range(N+1)]
    trip = [0] * (N+1)
    visited = [0] * (N+1)
    result = []
    for i in range(M):
        L, R = map(int, input().split())
        trip[R] += 1
        MAP[L].append(R)
    tripol = deque()
    for i in range(1, N+1):
        if trip[i] == 0:
            tripol.append(i)
    while tripol:
        a = tripol.popleft()
        result.append(a)
        for k in range(len(MAP[a])):
            trip[MAP[a][k]] -= 1
            if trip[MAP[a][k]] == 0:
                tripol.append(MAP[a][k])
    print("#{}".format(tc), end=' ')
    print(' '.join(list(map(str, result))))
