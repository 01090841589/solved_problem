import sys
sys.stdin = open("갤러리.txt")

N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
res = 0
flag = 1
for y in range(N - 1):
    for x in range(M):
        if MAP[y][x] == 'X':
            if flag:
                if MAP[y+1][x] == '.':
                    flag = 0
                else:
                    flag = 1
            else:
                if MAP[y+1][x] == '.':
                    flag = 1
                    res += 1
                else:
                    flag = 1
        else:
            flag = 1
for y in range(1, N):
    for x in range(M):
        if MAP[y][x] == 'X':
            if flag:
                if MAP[y-1][x] == '.':
                    flag = 0
                else:
                    flag = 1
            else:
                if MAP[y-1][x] == '.':
                    flag = 1
                    res += 1
                else:
                    flag = 1
        else:
            flag = 1
for x in range(M - 1):
    for y in range(N):
        if MAP[y][x] == 'X':
            if flag:
                if MAP[y][x+1] == '.':
                    flag = 0
                else:
                    flag = 1
            else:
                if MAP[y][x+1] == '.':
                    flag = 1
                    res += 1
                else:
                    flag = 1
        else:
            flag = 1
for x in range(1, M):
    for y in range(N):
        if MAP[y][x] == 'X':
            if flag:
                if MAP[y][x-1] == '.':
                    flag = 0
                else:
                    flag = 1
            else:
                if MAP[y][x-1] == '.':
                    flag = 1
                    res += 1
                else:
                    flag = 1
        else:
            flag = 1
print(res)