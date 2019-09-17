import sys
sys.stdin = open('길찾기.txt')

def bfs(n):
    for i in range(101):
        if visited[n][i] == 1:
            stack.append(i)
            visit[i] = 1
    while stack:
        k = stack.pop()
        for i in range(101):
            if visited[k][i] == 1:
                stack.append(i)
                visit[i] = 1
                if i == 99:
                    return

for tc in range(1, 11):
    t, N = map(int, input().split())
    node = list(map(int, input().split()))
    visited = [[0]*(101) for _ in range(101)]
    visit = [0] * 101
    for i in range(0, len(node), 2):
        visited[node[i]][node[i+1]] = 1
    stack = []
    bfs(0)
    print('#{} {}'.format(tc, visit[99]))