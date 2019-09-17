import sys
sys.stdin = open('pipe.txt')

DIR = [[[0,1]], [[0, 1], [1, 0], [1, 1]], [[1, 0]]]

def pipe(y, x, c):
    global result
    if x == N-1 or y == N-1:
        if x != N-1 and y != N-1:
            return
    if x == N-1 and y == N-1:
        result += 1
        return
    if c == 0:
        for a in range(2):
            flag = 0
            for b in DIR[a]:
                Y = y+b[0]
                X = x+b[1]
                if X < N and Y < N:
                    if MAP[Y][X] == 0:
                        continue
                    else:
                        flag = 1
                        break
            if X < N and Y < N and flag == 0:
                visited[Y][X] += 1
                pipe(Y, X, a)
    if c == 1:
        for a in range(3):
            flag = 0
            for b in DIR[a]:
                Y = y+b[0]
                X = x+b[1]
                if X < N and Y < N:
                    if MAP[Y][X] == 0:
                        continue
                    else:
                        flag = 1
                        break
            if X < N and Y < N and flag == 0:
                visited[Y][X] += 1
                pipe(Y, X, a)
    if c == 2:
        for a in range(1, 3):
            flag = 0
            for b in DIR[a]:
                Y = y+b[0]
                X = x+b[1]
                if X < N and Y < N:
                    if MAP[Y][X] == 0:
                        continue
                    else:
                        flag = 1
                        break
            if X < N and Y < N and flag == 0:
                visited[Y][X] += 1
                pipe(Y, X, a)
    # elif c == 1:

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
result = 0

visited = [[0]*N for _ in range(N)]
pipe(0, 1, 0)
[print(visited[i]) for i in range(N)]
print(result)