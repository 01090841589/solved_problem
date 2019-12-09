import sys
sys.stdin = open("하나로.txt")

def is_circle(node):
    global total
    if visited[node[1]] == -1 and visited[node[2]] == -1:
        visited[node[1]] = min(node[1], node[2])
        visited[node[2]] = min(node[1], node[2])
        total += node[0]
        return
    if visited[node[1]] != -1 and visited[node[2]] != -1:
        if visited[node[1]] == visited[node[2]]:
            return
        high = max(visited[node[1]], visited[node[2]])
        low = min(visited[node[1]], visited[node[2]])
        for a in range(N):
            if visited[a] == high:
                visited[a] = low
        total += node[0]
    else:
        dis = max(visited[node[1]], visited[node[2]])
        visited[node[1]] = dis
        visited[node[2]] = dis
        total += node[0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    island = [list(map(int, input().strip().split())) for _ in range(2)]
    cost = float(input())
    route = [[0]*N for _ in range(N)]
    total = 0
    distance = []
    for i in range(N-1):
        for j in range(i+1, N):
            dis = abs(island[0][i]-island[0][j])**2 + abs(island[1][i]-island[1][j])**2
            route[i][j] = dis
            route[j][i] = dis
            distance.append([dis, i, j])
    distance.sort()
    visited = [-1]*N
    for k in distance:
        is_circle(k)
        if visited.count(0) == len(visited):
            break
    print('#{} {}'.format(tc, round(total*cost)))