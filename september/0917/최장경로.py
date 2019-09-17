import sys
sys.stdin = open("최장경로.txt")

def dfs(k, visited, scr):
    global result
    if k > N:
        return
    for i in range(1, N+1):
        if MAP[k][i]:
            if visited[i]:
                continue
            visited[i] = 1
            dfs(i, visited, scr+1)
            visited[i] = 0
    if result < scr:
        result = scr


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(M)]
    # print('#{} {}'.format(tc, result))
    MAP = [[0]*(N+1) for _ in range(N+1)]
    result = 0
    for a in node:
        MAP[a[0]][a[1]] = 1
        MAP[a[1]][a[0]] = 1
    for i in range(1, N+1):
        visited = [0] * (N+1)
        visited[i] = 1
        dfs(i, visited, 1)
    print('#{} {}'.format(tc, result))