def num() :
    A, B = input().split(' ')
    A, B = int(A), int(B)
    a = input().split(' ')
    a = list(map(int,a))
    b = input().split(' ')
    b = list(map(int,b))
    if A > B :
        M = A
        N = B
        m = a
        n = b
    else :
        M = B
        N = A
        m = b
        n = a
    return M, N, m, n
def cal(M,N,m,n) :
    length = M-N
    max_num = 0
    cal_num = 0
    for i in range(length+1) :
        for j in range(N) :
            cal_num += (n[j] * m[i+j])
        if max_num < cal_num :
            max_num = cal_num
        cal_num = 0
    return cal_num,max_num

T = int(input())
for a in range(T) :
    M, N, m, n = num()
    cal_num,max_num = cal(M,N,m,n)
    print('#{0} {1}'.format(a+1,max_num))