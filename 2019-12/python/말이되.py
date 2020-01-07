import sys
sys.stdin = open("말이되고픈원숭이.txt")

K = int(input())

W, H = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(H)]

result = 987654321
dx = [0,0,-1,1]
dy = [-1,1,0,0]

hx = [-2,-1,1,2,-2,-1,1,2]
hy = [-1,-2,-2,-1,1,2,2,1]

visited = [[[999999999 for _ in range(K+1)] for _ in range(H)] for _ in range(W)]
def monkey(x,y, dist, hmove):
    global result
    if dist > result:
        return

    visited[y][x][hmove] = dist
    q = []
    q.append([x,y,dist, hmove])

    while q:
        t= q.pop(0)
        dist = t[2]
        hmove = t[3]
        if 0 < hmove:
            for k in range(8):
                nx = t[0] + hx[k]
                ny = t[1] + hy[k]
                if 0 <= nx < W and 0 <= ny < H and board[ny][nx] == 0:
                    if visited[ny][nx][hmove] > dist + 1:
                        visited[ny][nx][hmove] = dist + 1
                        if nx == W - 1 and ny == H - 1:
                            if result > dist+1:
                                result = dist+1
                        else:
                            q.append([nx, ny, dist+1, hmove-1])
        for k in range(4):
            nx = t[0] + dx[k]
            ny = t[1] + dy[k]

            if 0 <= nx < W and 0 <= ny < H and board[ny][nx] == 0:
                if visited[ny][nx][hmove] > dist+1:
                    visited[ny][nx][hmove] = dist + 1
                    if nx == W-1 and ny == H-1:
                        if result > dist+1:
                            result = dist+1
                    else:
                        q.append([nx,ny,dist+1, hmove])


    return -1

monkey(0,0,0,1)

if result == 987654321:
    result = -1



print(result)