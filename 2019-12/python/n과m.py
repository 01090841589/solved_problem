import sys
sys.stdin = open("nm.txt")

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

for y in range(N):
    for x in range(N):
        if MAP[y][x] == 0:
            for k in range(4):
                robot(y, x, k, 0)
