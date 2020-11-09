import sys
sys.stdin = open("2913.txt")

def bridge():
    for y in range(M):
        for x in range(N):
            if MAP[y][x] == '.':
                cnt = 0
                dir = 0
                for i, c in enumerate(DIR):
                    Y = y + c[0]
                    X = x + c[1]
                    if 0 <= Y < M and 0 <= X < N and MAP[Y][X] != '.':
                        if MAP[Y][X] in correct[i]:
                            cnt += 1
                            dir += 2 ** i
                if cnt == 2:
                    if dir % 3:
                        if dir // 10:
                            return y, x, '-'
                        else:
                            return y, x, '|'
                    else:
                        return y, x, ans[dir//3]
                if cnt == 4:
                    return y, x, '+'
M, N = map(int, input().split())
MAP = [list(input()) for _ in range(M)]
DIR = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 0011 0110 1100 1001
correct = [['2', '3', '|', '+'], ['3', '4', '-', '+'], ['4', '1', '|', '+'], ['1', '2', '-', '+']]
ans = [0, 1, 2, 4, 3]
# 01 10 / 01 -10 / 0-1-10 / 0-110
y, x, res = bridge()
print(y+1, x+1, res)