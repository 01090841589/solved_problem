import sys
sys.stdin = open('단어.txt')


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for x in range(N):
        ysis = []
        for y in range(N):
            ysis.append(MAP[y][x])
        MAP.append(ysis)
    for puzzle in MAP:
        k = 0
        for num in range(N):
            if puzzle[num] == 1:
                k += 1
            else :
                if k == K:
                    total += 1
                k = 0
            if num == N-1:
                if k == K:
                    total += 1
    print('#{} {}'.format(tc, total))
