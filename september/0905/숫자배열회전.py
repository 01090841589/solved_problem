import sys
sys.stdin = open('숫자배열회전.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for i in range(N)]
    MAP1, MAP2, MAP3 = [], [], []
    print(MAP)
    for i in range(N):
        MAP11, MAP22, MAP33 = [], [], []
        for j in range(N):
            MAP11.append(str(MAP[N-j-1][i]))
            MAP22.append(str(MAP[N-i-1][N-j-1]))
            MAP33.append(str(MAP[j][N-i-1]))
        MAP1.append(MAP11)
        MAP2.append(MAP22)
        MAP3.append(MAP33)
    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(MAP1[i]), ''.join(MAP2[i]), ''.join(MAP3[i]))