import sys
from collections import deque
sys.stdin = open("원판 돌리기.txt")

from collections import deque
DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def delete(y, x, k):
    global flag
    queue = deque()
    queue.append([y, x, k])
    while queue:
        y, x, k = queue.popleft()
        for c in DIR:
            Y = y+c[0]
            X = x+c[1]
            if X == -1:
                X = M-1
            if X == M:
                X = 0
            if 0 <= Y < N and MAP[Y][X] == k:
                flag = 0
                MAP[y][x] = 0
                MAP[Y][X] = 0
                queue.append([Y, X, k])


N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
order = [list(map(int, input().split())) for _ in range(K)]

# [print(MAP[i]) for i in range(N)]
# print()

for c in order:
    if c[1]:
        a = c[0]
        while a <= N:
            for i in range(c[2]):
                MAP[a-1].append(MAP[a-1].pop(0))
            a += c[0]
    else:
        a = c[0]
        while a <= N:
            for i in range(c[2]):
                MAP[a-1].insert(0, (MAP[a-1].pop()))
            a += c[0]
    # [print(MAP[i]) for i in range(N)]
    # print()

    flag = 1
    for y in range(N):
        for x in range(M):
            if MAP[y][x] > 0:
                delete(y, x, MAP[y][x])

    if flag:
        cnt = 0
        scr = 0
        for y in range(N):
            for x in range(M):
                if MAP[y][x] > 0:
                    cnt += 1
                    scr += MAP[y][x]
        if cnt == 0:
            break
        scr = scr / cnt
        for y in range(N):
            for x in range(M):
                if 0 < MAP[y][x] < scr:
                    MAP[y][x] += 1
                elif MAP[y][x] > scr:
                    MAP[y][x] -= 1

    # [print(MAP[i]) for i in range(N)]
    # print()
result = 0
for y in range(N):
    for x in range(M):
        if 0 < MAP[y][x]:
            result += MAP[y][x]
print('{}'.format(result))