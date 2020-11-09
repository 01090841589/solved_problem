import sys
sys.stdin = open("2913.txt")

M, N = map(int, input().split())
MAP = [list(input()) for _ in range(M)]
DIR = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 0011 0110 1100 1001
correct = [['2', '3', '|', '+'], ['3', '4', '-', '+'], ['4', '1', '|', '+'], ['1', '2', '-', '+']]
ans = [0, 1, 2, 4, 3]
# 01 10 / 01 -10 / 0-1-10 / 0-110
start, end = [], []
for y in range(M):
    for x in range(N):
        if MAP[y][x] == 'Z':
            start.append([y, x])
        elif MAP[y][x] == 'M':
            end.append([y, x])



print(y+1, x+1, res)