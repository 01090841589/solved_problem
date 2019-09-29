import sys
sys.stdin = open("인수의생일파티.txt")

from collections import deque
def back(x):
    queue = deque()
    queue.append(x)
    visited_1[x] = 0
    while queue:
        x = queue.popleft()
        for i in range(1, N+1):
            if MAP[i][x] > 0:
                if visited_1[i] > visited_1[x]+MAP[i][x]:
                    visited_1[i] = visited_1[x]+MAP[i][x]
                    queue.append(i)

def front(x):
    queue = deque()
    queue.append(x)
    visited_2[x] = 0
    while queue:
        x = queue.popleft()
        for i in range(1, N + 1):
            if MAP[x][i] > 0:
                if visited_2[i] > visited_2[x] + MAP[x][i]:
                    visited_2[i] = visited_2[x] + MAP[x][i]
                    queue.append(i)


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(M)]
    MAP = [[0]*(N+1) for _ in range(N+1)]
    for a in node:
        MAP[a[0]][a[1]] = a[2]
    total = 0
    visited_1 = [1234567]*(N+1)
    visited_2 = [1234567]*(N+1)
    back(X)
    front(X)
    for i in range(1, N+1):
        if total < visited_1[i]+visited_2[i]:
            total = visited_1[i]+visited_2[i]
    print('#{} {}'.format(tc, total))