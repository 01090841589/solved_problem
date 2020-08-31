import sys
sys.stdin = open("shortest.txt")

def SF(k):
    global result
    stack = [[k,0]]
    while stack:
        a, dis = stack.pop(0)
        if dis >= result:
            continue
        if a == G:
            if result > dis:
                result = dis
            continue
        for i in range(1, N+1):
            if visited[a][i] != 0:
                stack.append([i, dis+visited[a][i]])
                visited[a][i] = 0

T = int(input())
for tc in range(1, T+1):
    N, M, S, G = map(int,input().split())
    node = [list(map(int, input().split())) for _ in range(M)]
    visited = [[0] * (N+1) for _ in range(N+1)]
    result = 99999999
    for d in node:
        visited[d[0]][d[1]] = d[2]
        visited[d[1]][d[0]] = d[2]

    SF(S)
    print('#{} {}'.format(tc, result))