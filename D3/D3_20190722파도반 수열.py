T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    mat = [1, 1, 1, 2, 2]
    if N < 6:
        print('#{0} {1}'.format(test_case,mat[N-1]))
    else :
        for i in range(len(mat),N):
            mat.append(mat[i-1]+mat[i-5])
        print('#{0} {1}'.format(test_case,mat[N-1]))