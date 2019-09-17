import sys
sys.stdin = open('키순서.txt')

def win_bfs(k):
    global score
    visited = [0]*(N+1)
    visited[k] = 1
    stack = [k]
    while stack:
        n = stack.pop(0)
        for i in range(1, N+1):
            if win[n][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                score += 1

def lose_bfs(k):
    global score
    visited = [0]*(N+1)
    visited[k] = 1
    stack = [k]
    while stack:
        n = stack.pop(0)
        for i in range(1, N+1):
            if win[i][n] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                score += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = int(input())
    result = 0
    rank = [list(map(int, input().split())) for _ in range(M)]
    win = [[0]*(N+1) for _ in range(N+1)]
    lose = [[0]*(N+1) for _ in range(N+1)]
    for a in rank:
        win[a[0]][a[1]] = 1
        lose[a[1]][a[0]] = 1

    for i in range(1, N+1):
        score = 0
        win_bfs(i)
        lose_bfs(i)
        if score == N-1:
            result += 1
    print('#{} {}'.format(tc, result))