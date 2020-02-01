import sys
sys.stdin = open("막대기.txt")

def all_go():
    for Y in range(N):
        for X in range(M):
            if MAP[Y][X] and visited[Y][X] == 0:
                return False
    return True

def roll(y, x, status, scr):
    global result
    if scr > 10:
        return
    if all_go():
        if result > scr:
            result = scr
        return
    if status == 1:
        if x + 2 < M and MAP[y][x + 1] and MAP[y][x + 2]:
            visited[y][x + 1] += 1
            visited[y][x + 2] += 1
            roll(y, x+1, 2, scr+1)
            visited[y][x + 1] -= 1
            visited[y][x + 2] -= 1
        if y + 2 < N and MAP[y+1][x] and MAP[y+2][x]:
            visited[y + 1][x] += 1
            visited[y + 2][x] += 1
            roll(y+1, x, 3, scr+1)
            visited[y + 1][x] -= 1
            visited[y + 2][x] -= 1
        if 0 <= x - 2 and MAP[y][x - 1] and MAP[y][x - 2]:
            visited[y][x - 1] += 1
            visited[y][x - 2] += 1
            roll(y, x - 2, 2, scr + 1)
            visited[y][x - 1] -= 1
            visited[y][x - 2] -= 1
        if 0 <= y - 2 and MAP[y - 1][x] and MAP[y - 2][x]:
            visited[y - 1][x] += 1
            visited[y - 2][x] += 1
            roll(y-2, x, 3, scr+1)
            visited[y - 1][x] -= 1
            visited[y - 2][x] -= 1
    elif status == 2:
        if x + 2 < M and MAP[y][x + 2]:
            visited[y][x + 2] += 1
            roll(y, x+2, 1, scr+1)
            visited[y][x + 2] -= 1
        if y + 1 < N and MAP[y+1][x] and MAP[y+1][x+1]:
            visited[y + 1][x] += 1
            visited[y + 1][x + 1] += 1
            roll(y+1, x, 2, scr+1)
            visited[y + 1][x] -= 1
            visited[y + 1][x + 1] -= 1
        if 0 <= x - 1 and MAP[y][x - 1]:
            visited[y][x - 1] += 1
            roll(y, x-1, 1, scr+1)
            visited[y][x - 1] -= 1
        if 0 < y - 1 and MAP[y-1][x] and MAP[y-1][x+1]:
            visited[y - 1][x] += 1
            visited[y - 1][x + 1] += 1
            roll(y-1, x, 2, scr+1)
            visited[y - 1][x] -= 1
            visited[y - 1][x + 1] -= 1
    elif status == 3:
        if x + 1 < M and MAP[y][x + 1] and MAP[y + 1][x + 1]:
            visited[y][x + 1] += 1
            visited[y + 1][x + 1] += 1
            roll(y, x+1, 3, scr+1)
            visited[y][x + 1] -= 1
            visited[y + 1][x + 1] -= 1
        if y + 2 < N and MAP[y+2][x]:
            visited[y + 2][x] += 1
            roll(y+2, x, 1, scr+1)
            visited[y + 2][x] -= 1
        if 0 <= x - 1 and MAP[y][x - 1] and MAP[y + 1][x - 1]:
            visited[y][x - 1] += 1
            visited[y + 1][x - 1] += 1
            roll(y, x-1, 3, scr+1)
            visited[y][x - 1] -= 1
            visited[y + 1][x - 1] -= 1
        if 0 <= y - 1 < N and MAP[y-1][x]:
            visited[y - 1][x] += 1
            roll(y-1, x, 1, scr+1)
            visited[y - 1][x] -= 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    result = 100
    for y in range(N):
        for x in range(M):
            if MAP[y][x]:
                cnt += 1
    if cnt < 21:
        for y in range(N):
            for x in range(M):
                if MAP[y][x]:
                    visited[y][x] += 1
                    roll(y, x, 1, 1)
                    if x+1 < M:
                        visited[y][x+1] += 1
                        roll(y, x, 2, 1)
                        visited[y][x+1] -= 1
                    if y+1 < N:
                        visited[y+1][x] += 1
                        roll(y, x, 3, 1)
                        visited[y+1][x] -= 1
                    visited[y][x] -= 1

    if result == 100:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, result))

#주사위
