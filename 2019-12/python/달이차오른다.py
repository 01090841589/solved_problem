import sys
sys.stdin = open("달이차오른다.txt")


from collections import deque
N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
visited = [[[999999]*64 for _ in range(M) ] for __ in range(N)] # 열쇠를 가질수 있는 모든 경우의 수 : 64 만큼 visited 설정 최악의 경우의수 : 50*50*64 = 160000
start = [0, 0]
for y in range(N):
    for x in range(M):
        if MAP[y][x] == '0':
            start = [y, x] # 시작점
visited[start[0]][start[1]][0] = 0
MAP[start[0]][start[1]] = '.'
queue = deque([[start[0], start[1], 0, 0]])
result = 999999
while queue:
    y, x, dis, key = queue.popleft()
    for c in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        Y = y+c[0]
        X = x+c[1]
        if 0 <= Y < N and 0 <= X < M:
            if MAP[Y][X] == '.': # 길일때
                if visited[Y][X][key] > dis+1:
                    visited[Y][X][key] = dis+1
                    queue.append([Y, X, dis+1, key])
            elif 'A' <= MAP[Y][X] <= 'F': # 문일때
                door = (1 << (ord(MAP[Y][X])-65))
                open = key & door
                if open:
                    if visited[Y][X][key] > dis+1:
                        visited[Y][X][key] = dis+1
                        queue.append([Y, X, dis+1, key])
            elif 'a' <= MAP[Y][X] <= 'f': # 열쇠일때
                getkey = (1 << (ord(MAP[Y][X])-97))
                getkey = getkey & key # 열쇠가 이미있는지 확인
                if getkey == 0: # 열쇠가없으면 추가
                    getkey = key+(1 << (ord(MAP[Y][X])-97))
                    if visited[Y][X][getkey] > dis+1:
                        visited[Y][X][getkey] = dis+1
                        queue.append([Y, X, dis+1, getkey])
                else: # 열쇠가 있으면 pass
                    if visited[Y][X][key] > dis+1:
                        visited[Y][X][key] = dis+1
                        queue.append([Y, X, dis+1, key])

            elif MAP[Y][X] == '1':
                if result > dis+1:
                    result = dis+1

if result == 999999:
    print(-1)
else:
    print(result)
# [print(visited[i]) for i in range(N)]