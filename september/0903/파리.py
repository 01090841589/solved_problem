import sys
sys.stdin = open('파리.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    print('#{0} {1}'.format(tc, max([sum([sum(fly[i+a][j:j+M]) for a in range(M)]) for j in range(N-M+1) for i in range(N-M+1)])))