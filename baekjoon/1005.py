import sys
# sys.stdin = open("1005.txt")

import heapq

# sys.stdin.readline()
T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N, K = map(int, sys.stdin.readline().split())
    D = [0] + list(map(int, sys.stdin.readline().split()))
    MAP = [set() for _ in range(N+1)]
    MAP2 = [set() for _ in range(N+1)]
    cnt = 0
    for i in range(K):
        bef, aft = map(int, sys.stdin.readline().split())
        MAP[aft].add(bef)
        MAP2[bef].add(aft)
    G = int(sys.stdin.readline())
    start = []
    for i in range(1, N+1):
        if MAP[i] == set():
            heapq.heappush(start, [D[i], i])
    elasp = 0
    if MAP[G] == set():
        print(D[G])
    else:
        while MAP[G]:
            minv = start[0][0]
            elasp += minv
            v, k = heapq.heappop(start)
            for i in range(len(start)):
                start[i][0] -= minv

            for node in MAP2[k]:
                MAP[node].discard(k)
                if MAP[node] == set():
                    heapq.heappush(start, [D[node], node])

        print(elasp+D[G])
