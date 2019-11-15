from collections import deque
import sys
sys.stdin = open("홈 방범 서비스.txt")

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    global ans
    h = 0
    if nxn[x][y] == 1:
        h = 1
    Q = deque()
    Q.append((x, y))
    visited[x][y] = 1

    while len(Q):
        x, y = Q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                if nxn[nx][ny] == 1:
                    h += 1
                if visited[nx][ny] < K:
                    Q.append((nx, ny))

    if h * M >= K**2 + (K-1)**2:
        if h > ans:
            ans = h


T = int(input())

for test in range(T):
    N, M = map(int, input().split())
    nxn = [[0 for _ in range(N)]for _ in range(N)]



    for z in range(N):
        nxn[z] = list(map(int, input().split()))
    K = 0
    cnt = 0
    ans = 0
    # 최대 비용을 찾기위한 써치
    for x in range(N):
        for y in range(N):
            if nxn[x][y] == 1:
                cnt += 1

    price = cnt * M
    # 최대비용으로 가능한 K값 구하기 이후에 써치하면서 K -1 씩하면서 정답 구하기
    for k in range(1, 30):
        kk = k**2 + (k-1)**2
        if kk > price:
            K = k - 1
            break
    RK = K

    for z in range(K):
        K = RK
        K = K - z
        for x in range(N):
            for y in range(N):
                visited = [[0 for _ in range(N)] for _ in range(N)]
                bfs(x, y)

    print("#%d %d" % (test+1, ans))