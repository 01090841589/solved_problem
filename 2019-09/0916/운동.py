import sys
sys.stdin = open("운동.txt")

def cycle():
    print('#{} {}'.format(tc, 3))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    node = [list(map(int, input().split())) for _ in range(M)]
    visited = [[0] * (N+1) for _ in range(N+1)]
    for d in node:
        visited[d[0]][d[1]] = d[2]
    # [print(visited[i]) for i in range(N+1)]
    cycle()