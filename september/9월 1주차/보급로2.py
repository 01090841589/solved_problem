import sys
sys.stdin = open('보급로.txt')
DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
DIR2 = [[0, 1], [1, 0]]

def short_search(y, x, n, visited):
    global score
    if y == 0 and x == 0:
        visited[y][x] = 1
    if y == N-1 and x == N-1:
        score = n
    else:
        comp = 99
        go = []
        for c in DIR2:
            Y = y+c[0]
            X = x+c[1]
            if 0 <= X < N and 0 <= Y < N and visited[Y][X] == 0:
                if MAP[Y][X] < comp:
                    go = [Y, X]
                    comp = MAP[Y][X]
        visited[go[0]][go[1]] = 1
        short_search(go[0], go[1], n+MAP[go[0]][go[1]], visited)

def DFS(y, x, n, visited):
    global result
    if y == 0 and x == 0:
        visited[y][x] = 1
    if n >= result:
        return
    if y == N-1 and x == N-1:
        if result > n:
            result = n
            return
    else:
        for c in DIR:
            Y = y+c[0]
            X = x+c[1]
            if 0 <= X < N and 0 <= Y < N and visited[Y][X] == 0:
                visited[Y][X] = 1
                DFS(Y, X, n + MAP[Y][X], visited)
                visited[Y][X] = 0   

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]
    # [print(MAP[i]) for i in range(N)]
    score = 0
    short_search(0, 0, 0, [[0]*N for _ in range(N)])
    result = score
    DFS(0, 0, 0, [[0]*N for _ in range(N)])
    print(result)