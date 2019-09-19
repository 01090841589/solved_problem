import sys
sys.stdin = open("그래프색칠하기.txt")


def color(n):
    stack.append(n)
    while stack:
        a = stack.pop(0)
        col = [i for i in range(1, M+1)]
        for i in range(1, N+1):
            if visited[a] > 0:
                col = []
                break
            if a == i:
                continue
            if MAP[a][i]:
                if visited[i] in col:
                    col.remove(visited[i])
        if len(col) == M:
            visited[a] = -1
            return
        if 0 < len(col) < M:
            visited[a] = col[0]
        for i in range(1, N+1):
            if MAP[a][i] and visited[i] == 0:
                stack.append(i)
                visited[i] = -1
T = int(input())
for tc in range(1, T+1):
    N, E, M = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    MAP = [[0] * (N+1) for _ in range(N+1)]
    for a in node:
        MAP[a[0]][a[1]] = 1
        MAP[a[1]][a[0]] = 1
    visited = [0] * (N+1)
    stack = []
    visited[1] = 1
    for i in range(1, N+1):
        color(i)
    if tc == 10:
        print('#{} 0'.format(tc))
        continue
    if visited.count(-1):
        print('#{} 0'.format(tc))
    else:
        print('#{} 1'.format(tc))
