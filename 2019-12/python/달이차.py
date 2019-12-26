import sys

sys.stdin = open("달이차오른다.txt")

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N, M = map(int, input().split())

laby = [list(input()) for _ in range(N)]
visited = [[[999999 for _ in range(M)] for _ in range(N)] for _ in range(64)]

for i in range(N):
    for j in range(M):
        if laby[i][j] == "0":
            minsic = [j,i]
            laby[i][j] = "."

# print(visited)
#
# print(list(map(ord, ["a", "f", "A", "F"])))

def bfs(x,y,d,dist):
    global result
    visited[d][y][x] = dist
    q = []
    q.append([x,y,0, 0])

    while q:
        t = q.pop(0)
        for k in range(4):
            nx = t[0] + dx[k]
            ny = t[1] + dy[k]
            d = t[2]
            dist = t[3]
            if 0 <= nx <M and 0 <= ny <N and visited[d][ny][nx] == 999999:
                if laby[ny][nx] == '.':
                    if visited[d][ny][nx] > 1 + dist:
                        visited[d][ny][nx] = 1 + dist
                        q.append([nx, ny, d, 1+dist])

                elif 97 <= ord(laby[ny][nx]) <= 102:
                    if (2**(ord(laby[ny][nx])-97) & d):
                        if visited[d][ny][nx] > 1 + dist:
                            visited[d][ny][nx] = 1 + dist
                            q.append([nx, ny, d, 1+dist])
                    else:
                        tem = 2**(ord(laby[ny][nx])-97)
                        if visited[d+tem][ny][nx] > 1 + dist:
                            visited[d+tem][ny][nx] = 1 + dist
                            q.append([nx, ny, d+tem, 1+dist])
                elif 65 <= ord(laby[ny][nx]) <= 70:
                    if (2**(ord(laby[ny][nx])-65)) & d:
                        if visited[d][ny][nx] > 1 + dist:
                            visited[d][ny][nx] = 1 + dist
                            q.append([nx, ny, d, 1+dist])
                elif laby[ny][nx] == '1':
                    if visited[d][ny][nx] > 1+ dist:
                        visited[d][ny][nx] = 1+dist
                        if result > visited[d][ny][nx]:
                            result = visited[d][ny][nx]

result = 999999

bfs(minsic[0],minsic[1],0,0)


if result == 999999:
    result = -1

print(result)