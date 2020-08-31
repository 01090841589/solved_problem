import sys
sys.stdin = open('인구이동.txt')

N, L, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] *N for _ in range(N)]
a = 1
result = 0
while True:
    comp_MAP = [MAP[i][:] for i in range(N)]

    for y in range(N):
        for x in range(N):
            if visited[y][x] == 0:
                flag = 0
                if x+1 < N:
                    if L <= abs(MAP[y][x] - MAP[y][x+1]) <= R:
                        visited[y][x] = a
                        visited[y][x+1] = a
                        flag = 1
                if y+1 < N:
                    if L <= abs(MAP[y][x] - MAP[y+1][x]) <= R:
                        visited[y][x] = a
                        visited[y+1][x] = a
                        flag = 1
                if x-1 >= 0:
                    if L <= abs(MAP[y][x] - MAP[y][x-1]) <= R:
                        visited[y][x] = a
                        visited[y][x-1] = a
                        flag = 1
                if y - 1 >= N:
                    if L <= abs(MAP[y][x] - MAP[y - 1][x]) <= R:
                        visited[y][x] = a
                        visited[y - 1][x] = a
                        flag = 1


                if flag:
                    a += 1
            else:
                if x + 1 < N:
                    if L <= abs(MAP[y][x] - MAP[y][x + 1]) <= R:
                        visited[y][x + 1] = visited[y][x]
                if y + 1 < N:
                    if L <= abs(MAP[y][x] - MAP[y + 1][x]) <= R:
                        visited[y + 1][x] = visited[y][x]
                if x-1 >= 0:
                    if L <= abs(MAP[y][x] - MAP[y][x-1]) <= R:
                        visited[y][x-1] = visited[y][x]
                if y - 1 >= N:
                    if L <= abs(MAP[y][x] - MAP[y - 1][x]) <= R:
                        visited[y - 1][x] = visited[y][x]
    for num in range(1, a):
        people = 0
        cnt = 0
        for y in range(N):
            for x in range(N):
                if visited[y][x] == num:
                    people += MAP[y][x]
                    cnt += 1
        for y in range(N):
            for x in range(N):
                if visited[y][x] == num:
                    MAP[y][x] = people//cnt
    if comp_MAP == MAP:
        break
    result += 1


print(result)