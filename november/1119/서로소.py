import sys
sys.stdin = open("서로소.txt")


def UF(n):
    if visited[n] == n:
        return n
    visited[n] = UF(visited[n])
    return visited[n]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(M)]
    visited = [i for i in range(N+1)]
    print('#{} '.format(tc),end='')
    for c in node:
        if c[0] == 0:
            n1 = UF(c[1])
            n2 = UF(c[2])
            if n1 < n2:
                visited[c[2]] = n1
            else:
                visited[c[1]] = n2
        elif c[0] == 1:
            n1 = UF(c[1])
            n2 = UF(c[2])
            if n1 == n2:
                print(1, end='')
            else:
                print(0, end='')
    print()

