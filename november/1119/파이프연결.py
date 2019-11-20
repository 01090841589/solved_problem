import sys
sys.stdin = open("파이프연결.txt")

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
PIPE = [[1, 3], [0, 2], [1, 2], [2, 3], [3, 0], [0, 1]]


from collections import deque

T = int(input())
for tc in range(1, 2):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    que = deque([[0, 0, 0, 0, 0]])
    visited[0][0] = 1
    while que:
        y, x, scr, k, pip = que.popleft()
        if y == N-1 and x == N-1:
            print(y, x, scr, k, pip)
            # if pip == 0 and k == 1:
            #
            # elif pip == 5 and k == 0:

        for c in PIPE[k]:
            Y = y+DIR[c][0]
            X = x+DIR[c][1]
            if 0 <= X < N and 0 <= Y < N and visited[Y][X] < 5:
                print(c)
                if 0 <= MAP[Y][X] <= 1:
                    for p in range(2):
                        if (c+2)%4 in PIPE[p]:
                            visited[Y][X] += 1
                            for m in PIPE[p]:
                                if m != (c+2)%4:
                                    s = m
                            que.append([Y, X, scr+1, s, p])
                else:
                    for p in range(2, 6):
                        if (c+2)%4 in PIPE[p]:
                            visited[Y][X] += 1
                            for m in PIPE[p]:
                                if m != (c+2)%4:
                                    s = m
                            que.append([Y, X, scr+1, s, p])

