def mat(N) :
    for i in range(N) :
        mat = input().split(' ')
        # mat = list(map(int,mat))
        matrix.append(mat)
    return matrix

def cal_mat(matrix) :
    matrix_90 = []
    matrix_180 = []
    matrix_270 = []
    num = ''
    for i in range(len(matrix)) :
        for j in range(len(matrix)) :
            num += matrix[len(matrix)-1-j][i]
        matrix_90.append(num)
        num = ''
    for i in range(len(matrix)) :
        for j in range(len(matrix)) :
            num += matrix[len(matrix)-1-i][len(matrix)-1-j]
        matrix_180.append(num)
        num = ''
    for i in range(len(matrix)) :
        for j in range(len(matrix)) :
            num += matrix[j][len(matrix)-1-i]
        matrix_270.append(num)
        num = ''
    return matrix_90,matrix_180,matrix_270
T = int(input())
for a in range(T):
    N = int(input())
    matrix = []
    matrix = mat(N)
    matrix_90,matrix_180,matrix_270 = cal_mat(matrix)
    print('#{0}'.format(a+1))
    for b in range(len(matrix)) :
        print('{0} {1} {2}'.format(matrix_90[b],matrix_180[b],matrix_270[b]))