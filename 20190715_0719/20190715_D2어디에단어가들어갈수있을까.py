N = 5
K = 3
def matrix(N) :
    mat = []
    for i in range(N) :
        inp = input().split(' ')
        inp = [x for x in inp if x]
        inp = list(map(int,inp))
        mat.append(inp)
    return mat
def cal_stat(mat) :
    length = 0
    answer = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 1 :
                length += 1
                if j < len(mat)-1 :
                    if mat[i][j+1] == 1 :
                        continue
                    else :
                        if length == K :
                            answer += 1
                        length = 0
            if length == K:
                answer += 1
        length = 0
    for j in range(len(mat)):
        for i in range(len(mat)):
            if mat[i][j] == 1 :
                length += 1
                if i < len(mat)-1 :
                    if mat[i+1][j] == 1 :
                        continue
                    else :
                        if length == K :
                            answer += 1
                        length = 0
            if length == K:
                answer += 1
        length = 0
    return answer
T = int(input())
for a in range(T) :
    N, K = input().split(' ')
    N = int(N)
    K = int(K)
    mat = matrix(N)
    print('#{0} {1}'.format(a+1,cal_stat(mat)))