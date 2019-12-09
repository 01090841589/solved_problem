import sys
sys.stdin = open("최소스패닝.txt")

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    node = [[node[i][2],node[i][0],node[i][1]] for i in range(E)]
    node.sort()
    visited = [-1]*(V+1)
    result = 0
    cnt = 0
    for i in range(E):
        if cnt = V:
            print('#{} {}'.format(tc, result))
            break
        if visited[node[i][1]] == -1 and visited[node[i][2]] == -1:
            visited[node[i][1]] = min(node[i][1], node[i][2])
            visited[node[i][2]] = min(node[i][1], node[i][2])
            result += node[i][0]
            cnt += 2
        elif visited[node[i][1]] == visited[node[i][2]]:
            continue
        elif visited[node[i][1]] == -1 or visited[node[i][2]] == -1:
            if visited[node[i][1]] == -1:
                visited[node[i][1]] = visited[node[i][2]]
            if visited[node[i][2]] == -1:
                visited[node[i][2]] = visited[node[i][1]]
            result += node[i][0]
        else:
            high = max(visited[node[i][1]] , visited[node[i][2]])
            low = min(visited[node[i][1]] , visited[node[i][2]])
            for j in range(V+1):
                if visited[j] == high:
                    visited[j] = low
            result += node[i][0]
