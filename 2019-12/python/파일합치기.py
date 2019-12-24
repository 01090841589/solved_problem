import sys
sys.stdin = open("파일합치기.txt")

T = int(input())
for t in range(T):
    K = []
    file = []
    K.append(int(input()))
    file.append(list(map(int, input().split())))
    k = K[0]
    f = file[0]
    sum = [f[0]]
    for i in f[1:]:
        sum.append(i + sum[-1])
    filesum = [[0] * k for _ in range(k)]
    filesum[0][1] = sum[1]
    for i in range(1, k - 1):
        filesum[i][i + 1] = sum[i + 1] - sum[i - 1]
    for gap in range(2, k):
        for i in range(k - gap):
            filesum[i][i + gap] = float('inf')
            for j in range(i, i + gap):
                filesum[i][i + gap] = min(filesum[i][i + gap], filesum[i][j] + filesum[j + 1][i + gap])
            if i > 0:
                filesum[i][i + gap] = filesum[i][i + gap] + sum[i + gap] - sum[i - 1]
            else :
                filesum[i][i + gap] = filesum[0][gap] + sum[gap]
    print('#{} {}'.format(t+1, filesum[0][k - 1]))
