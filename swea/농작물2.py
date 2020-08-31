import sys
sys.stdin = open('농작물.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    MAP = [list(input()) for _ in range(N)]
    SUM = [int(MAP[y][x]) for y in range(N) for x in range(abs(y-N//2), N-abs(y-N//2))]
    print('#{} {}'.format(tc,sum(SUM)))
