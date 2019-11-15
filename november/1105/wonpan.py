import sys
from collections import deque
sys.stdin = open("원판 돌리기.txt")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# bfs 를 통해 인접하면서 같은수 제거하는 함수
def bfs(x, y):
    cnt = 0
    tmp = nxm[x][y]
    Q = deque()
    Q.append((x, y))

    while len(Q):
        x, y = Q.popleft()

        for d in range(4):
            nx = (x + dx[d])
            ny = (y + dy[d]) % M
            if 0 <= nx < N and 0 <= ny < M:
                if nxm[nx][ny] == tmp:
                    nxm[nx][ny] = 0
                    cnt += 1
                    Q.append((nx, ny))
    if cnt > 0:
        return 1
    else:
        return 0

# 원판을 회전 시킨후 지워지는 숫자가 있나 체크하는 함수
def check(num, dir, t):
    global flag
    while t > 0:
        if dir == 0:
            for n in range(1, 26):
                v = (num * n) - 1
                if v < N:
                    tmp = nxm[v].pop()
                    nxm[v].appendleft(tmp)
                else:
                    break
        else:
            for n in range(1, 26):
                v = (num * n) - 1
                if v < N:
                    tmp = nxm[v].popleft()
                    nxm[v].append(tmp)
                else:
                    break
        t -= 1

    for q in range(N):
        v = q
        if v <= N:
            for i in range(M):
                if nxm[v][i] > 0:
                    if bfs(v, i):
                        nxm[v][i] = 0
                        flag = 1

        else:
            break


N, M, T = map(int, input().split())
nxm = [deque(list(map(int, input().split()))) for _ in range(N)]

avg = 0
ans = 0
arr = []
for z in range(T):
    a, b, c = map(int, input().split())
    arr.append((a, b, c))

for z in range(T):
    flag = 0
    check(arr[z][0], arr[z][1], arr[z][2])

    # 원판 회전후 지워지는 숫자가 없을때
    if flag == 0:
        sum = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if nxm[i][j] > 0:
                    sum += nxm[i][j]
                    cnt += 1
        if cnt > 0:
            avg = sum / cnt
            for i in range(N):
                for j in range(M):
                    if nxm[i][j] > 0:
                        if nxm[i][j] > avg:
                            nxm[i][j] -= 1
                        elif nxm[i][j] < avg:
                            nxm[i][j] += 1

for i in range(N):
    for j in range(M):
        if nxm[i][j] > 0:
            ans += nxm[i][j]

print(ans)