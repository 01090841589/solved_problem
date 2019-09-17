import sys
sys.stdin = open('파스칼.txt')

PASCAL = [[0]*11 for i in range(1,12)]
PASCAL[0][1] = 1
for i in range(1,11):
    for j in range(1, i+1):
        PASCAL[i][j] = PASCAL[i-1][j]+PASCAL[i-1][j-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    for i in range(1, 1+N):
        for j in range(1, i+1):
            print(PASCAL[i][j], end=' ')
        print()
