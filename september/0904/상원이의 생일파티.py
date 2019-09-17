import sys
sys.stdin = open('생일파티.txt')

def bfs(n):
    global result
    queue = [n]
    visited[n] = 1
    k = 0
    cnt = 0
    while queue:
        k += 1
        m = queue.pop(0)
        if visited[m] == 3:
            result = cnt
            return
        for i in range(N+1):
            if MAP[m][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[m]+1
                if visited[m] <=2:
                    cnt += 1



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    rela = [list(map(int, input().split())) for _ in range(M)]
    MAP = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    result = 0
    for c in rela:
        MAP[c[0]][c[1]] = 1
        MAP[c[1]][c[0]] = 1

    bfs(1)
    print('#{} {}'.format(tc, result))