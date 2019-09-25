import sys
sys.stdin = open('정사각형방.txt')

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(ni, nj):
    cnt = 1
    go = True
    while go:
        go = False
        i, j = ni, nj
        visit[A[i][j]] = True
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            if -1 < ni < N and -1 < nj < N and A[ni][nj] == A[i][j] + 1:
                if dp[A[ni][nj]]:
                    cnt += dp[A[ni][nj]]
                    return cnt
                go = True
                cnt += 1
                break
    return cnt


for tc in range(1, int(input()) + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    NN = N * N
    visit = [False] * (NN + 1)
    dp = [0] * (NN + 1)
    ans = 0
    for i in range(N):
        for j in range(N):
            if not visit[A[i][j]] and ans <= NN - A[i][j]:
                cnt = bfs(i, j)
                dp[A[i][j]] = cnt
                if cnt == ans:
                    if A[i][j] < room:
                        room = A[i][j]
                elif cnt > ans:
                    ans = cnt
                    room = A[i][j]
    print('#{} {} {}'.format(tc, room, ans))