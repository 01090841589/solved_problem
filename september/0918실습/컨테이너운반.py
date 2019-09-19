import sys
sys.stdin = open("컨테이너운반.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    W.sort(reverse=True)
    T = list(map(int, input().split()))
    T.sort(reverse=True)
    visited = [0] * M
    total = 0
    for a in W:
        for i in range(M):
            if a <= T[i] and visited[i] == 0:
                visited[i] = 1
                total += a
                break
    print('#{} {}'.format(tc, total))