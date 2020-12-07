import sys
sys.stdin = open("18224.txt")

n,m = map(int, input().split())

miro = [list(map(int, input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]
visited = [[[n*n] * m for _ in range(n)] for _ in range(n)]
from collections import deque
def escape():
    visited[0][0][0] = 1
    q = deque()
    q.append([0,0,1,1,0]) # x,y,날짜,낮밤, movecnt
    while q:
        tx, ty, date, day, cnt = q.popleft()
        nday = day
        ndate = date
        ncnt = cnt+1
        if not (cnt+1)%m :
            nday = (day+1)%2
            if day == 0:
                ndate = ndate+1
            ncnt = 0

        if day == 1:
            for k in range(4):
                nx, ny = tx+dx[k], ty+dy[k]
                if 0<=nx<n and 0<=ny <n:
                    if miro[ny][nx]==0 :
                        q.append([nx, ny, ndate, nday, ncnt])
                        if nx == n - 1 and ny == n - 1:
                            return (ndate, nday)

        else:
            for k in range(4):
                nx,ny = tx, ty
                flag = 0
                while 1:
                    temx, temy = nx + dx[k], ny + dy[k]
                    if 0 <= temx < n and 0 <= temy < n:
                        if miro[temy][temx] == 0:
                            nx, ny = temx, temy
                            flag = 1
                            break
                        else:
                            nx, ny = temx, temy
                    else:
                        break

                if flag :
                    if miro[ny][nx] == 0 :
                        if visited[ty][tx][ncnt]+1 < visited[ny][nx][ncnt]:
                            visited[ny][nx][ncnt] = visited[ty][tx][ncnt]+1
                            q.append([nx, ny, ndate, nday, ncnt])
                            if nx == n-1 and ny == n-1:
                                return (ndate, nday)
    return (-1,-1)


if n == 1:
    print(1, "sun")
else:
    adate, aday = escape()

    [print(visited[i]) for i in range(n)]
    if adate == -1:
        print(-1)

    else:
        if aday == 1:
            print(adate, "sun")
        else:
            print(adate, "moon")