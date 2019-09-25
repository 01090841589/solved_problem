import sys
sys.stdin = open('최소이동거리.txt')


def bfs(k):
    stack = [k]
    while stack:
        a = stack.pop(0)
        for i in range(N+1):
            if MAP[a][i] != 0:
                if visit[i] > visit[a] + MAP[a][i]:
                    visit[i] = visit[a] + MAP[a][i]
                    stack.append(i)


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    MAP = [[0] * (N+1) for _ in range(N+1)]
    for a in node:
        MAP[a[0]][a[1]] = a[2]
    visit = [(N+1)*10 for _ in range(N+1)]
    visit[0] = 0
    bfs(0)
    print('#{} {}'.format(tc, visit[N]))