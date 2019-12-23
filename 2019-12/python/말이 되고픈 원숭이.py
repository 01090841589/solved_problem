import sys
sys.stdin = open("말이되고픈원숭이.txt")

from collections import deque
DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
DIR2 = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]


def monkeyhorse(y, x, k):

K = int(input())
W, H = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(H)]
[print(MAP[i]) for i in range(H)]
visited = [[[0]*(K+1) for _ in range(H)] for __ in range(W)]
# for y in range(H):
#     for x in range(W):
#         if MAP[y][x]:
#             for i in range(K+1):
#                 visited[y][x][i] = 1
monkeyhorse(0, 0, K)

        if k > 0:
            for c in DIR2:
                Y = y + c[0]
                X = x + c[1]
                if 0 <= Y < H and 0 <= X < W:
                    if MAP[Y][X] == 0 and visited[Y][X][k] == 0:
        for c in DIR:
            Y = y + c[0]
            X = x + c[1]

        pass
[print(visited[i])for i in range(H)]