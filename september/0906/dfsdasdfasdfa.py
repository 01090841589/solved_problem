import sys
sys.stdin = open('격자판.txt')

def wall(y,x):
    if y < 0 or y > 3  : return False
    if x < 0 or x > 3 : return False
    return True

def follow(y,x, k):
    global cnt, visited
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if k >= 7:
            return
        if wall(ny,nx) == True:
            visited[ny][nx] = visited[y][x]+1
            if visited[ny][nx] == 6:
                cnt += 1
            return follow(ny,nx, k+1)

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

T = int(input())
for tc in range(T):
    grid = [list(map(int, input().split())) for _ in range(4)]
    visited = [[0 for _ in range(4)] for _ in range(4)]
    box = []
    cnt = 0
    for y in range(4):
        for x in range(4):
            follow(y,x, 0)
            visited = [[0 for _ in range(4)] for _ in range(4)]
    print(cnt)
