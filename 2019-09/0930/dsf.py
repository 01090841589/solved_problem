import sys
sys.stdin = open("외판원.txt")


def dfs(x, sum, depth, key):
    if sum >= ans[0]:
        return
    if depth == N and x == key:
        ans[0] = sum
    for y in range(N):
        if nxn[x][y] > 0 and visited[y] == 0:
            visited[y] = 1
            dfs(y, sum+nxn[x][y], depth+1, key)
            visited[y] = 0
N = int(input())

nxn = [[0 for _ in range(N)]for _ in range(N)]

ans = [1e9]

for z in range(N):
    nxn[z] = list(map(int, input().split()))


for i in range(N):
    for j in range(N):
        if nxn[i][j] > 0:
            visited = [0 for _ in range(N)]
            visited2 = [0 for _ in range(N)]
            dfs(i, 0, 0, i)

print(ans[0])