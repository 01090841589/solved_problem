import sys
sys.stdin = open('수제버거.txt')

def part(N, k, ham):
    global total
    if len(ham) > 1:
        for i in range(len(ham)-1):
            for j in range(i+1, len(ham)):
                if hater[ham[i]-1][ham[j]-1]:
                    return
    if N == k :
        total += 1
        return
    part(N, k+1, ham+[ingre[k]])
    part(N, k+1, ham)
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ingre = [i for i in range(1, N+1)]
    hate = [list(map(int, input().split())) for _ in range(M)]
    hater = [[0]*N for _ in range(N)]
    for a in hate:
        hater[a[0]-1][a[1]-1] = 1
        hater[a[1]-1][a[0]-1] = 1
    total = 0
    part(N, 0, [])
    print('#{} {}'.format(tc, total))