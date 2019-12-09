import sys
sys.stdin = open('동서양의경계.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [list(input()) for _ in range(M)]
    result = 999999
    resi1 = 0
    WE = []
    for j in range(N+1):
        west = 0
        east = 0
        for i in range(M):
            if result <= west+east:
                break
            west += MAP[i][:j].count('E')
            east += MAP[i][j:].count('W')
        if result > west+east:
            result = west+east
            resi1 = j
        if result == 0:
    print('#{} {}'.format(tc, resi1, resi1+1))