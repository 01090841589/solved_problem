import sys

sys.stdin = open('20058.txt')

N,Q = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(2**N)]

# print(grid)

Ls = list(map(int, input().split()))
# print(Ls)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def rot(x,y,w):
    mos = [[x,y],[x+w-1,y],[x+w-1,y+w-1], [x,y+w-1],]
    c = 0
    tx, ty = x, y
    tem = [[0 for _ in range(w)] for _ in range(4)]
    tx,ty = x, y

    for i in range(4):
        x,y = mos[i]
        for j in range(w):
            nx, ny = x+dx[i]*j, y+dy[i]*j
            tem[i][j] = grid[ny][nx]

    for i in range(4):
        x,y = mos[i]
        for j in range(w):
            nx, ny = x + dx[i] * j, y + dy[i] * j
            grid[ny][nx] = tem[i-1][j]

def melt(x,y):
    cnt = 0
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<= nx<2**N and 0<= ny <2**N:
            if grid[ny][nx] :
                cnt += 1

    if cnt < 3 :
        candi.append([x,y])


def bfs(x,y):
    global ans, ice
    cnt = 1
    q = []
    visited[y][x] = 1
    q.append([x,y])
    while q:
        tx,ty = q.pop(0)
        for k in range(4):
            nx, ny = tx+dx[k], ty+dy[k]
            if 0 <= nx < 2**N and 0 <= ny < 2**N:
                if grid[ny][nx] and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([nx,ny])
                    ice += grid[ny][nx]
                    cnt += 1
    if ans < cnt:
        ans = cnt

for a in range(Q):
    L = Ls[a]
    wid = 2**L
    num = 2**(N-L)
    if L != 0:
        print(L)
        for i in range(0,2**N,wid):
            for j in range(0,2**N,wid):
                for d in range(L):
                    sx,sy = j+1*d, i+1*d
                    rot(sx,sy,wid-(2*d))

    for _ in range(2**N):
        print(grid[_])
    print()

    candi = []
    for row in range(2**N):
        for col in range(2**N):
            if grid[row][col]:
                melt(col,row)
    for ax,ay in candi:
        grid[ay][ax] -= 1

    for _ in range(2**N):
        print(grid[_])
    print()


ans = 0
ice = 0
visited = [[0 for _ in range(2**N)] for _ in range(2**N)]
for i in range(2**N):
    for j in range(2**N):
        if grid[i][j] and visited[i][j] == 0:
            ice += grid[i][j]
            bfs(j,i)

print(ice)
print(ans)