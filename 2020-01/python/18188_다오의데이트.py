import sys
sys.stdin = open("다오의데이트.txt")

DIR = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def go_dao(y, x, k, route):
    global result, rts
    if result:
        return
    if k >= A:
        return
    flag = 1
    for i in range(4):
        if can[k][i]:
            Y = y+DIR[i][0]
            X = x+DIR[i][1]
            if 0 <= Y < H and 0 <= X < W:
                if MAP[Y][X] != '@':
                    if MAP[Y][X] == 'Z':
                        rts = route+arr[i]
                        result = 1
                        return
                    flag = 0
                    go_dao(Y, X, k+1, route+arr[i])
    if flag:
        pass


H, W = map(int, input().split())
MAP = [list(input()) for _ in range(H)]
for h in range(H):
    for w in range(W):
        if MAP[h][w] == 'D':
            y = h
            x = w
result = 0
rts = ''
A = int(input())
arr = ['W', 'D', 'S', 'A']
can = [[0, 0, 0, 0] for _ in range(A)]
for i in range(A):
    B, C = map(str, input().split())
    can[i][arr.index(B)] = 1
    can[i][arr.index(C)] = 1

go_dao(y, x, 0, '')
if result:
    print("YES")
    print(rts)
else:
    print("NO")
