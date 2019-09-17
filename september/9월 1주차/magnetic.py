import sys
sys.stdin = open('mag.txt')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for i in range(N)]
    total = 0
    for x in range(N):
        NS = ''
        for y in range(N):
            if mat[y][x] != 0:
                NS += str(mat[y][x])
        for i in range(len(NS)-1):
            if NS[i]+NS[i+1]=='12':
                total += 1
    print('#{} {}'.format(test_case,total))