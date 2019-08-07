T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    mat = []
    for a in range(N):
        mat.append(input())
    sum = 0
    for i in range(N):
        if i < N//2+1:
            for j in range(N//2-i,N//2+i+1):
                sum += int(mat[i][j])
        elif i >= N//2+1:
            for j in range(N//2+i+1-N,N//2-i+N):
                sum += int(mat[i][j])
    print('#{} {}'.format(test_case,sum))