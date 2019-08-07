

def corr(lst):
    temp = 0
    fail = 0
    for i,j in enumerate(lst):
        if i == 0:
            temp = j
        elif temp > j :
            if temp-j == 1:
                temp = j
                k = i-1
                for a in range(NX[1]):
                    k += 1
                    if 0<= k < (NX[0]):
                        if lst[k] == temp and AA[k] == 0:
                            AA[k] = 1
                        else :
                            fail = 1
                    else:
                        fail = 1
            else:
                fail = 1
        elif temp < j:
            temp = j
    return fail
def forwbackw(lst):
    fai = 0
    fai += corr(lst)
    lst.reverse()
    AA.reverse()
    fai += corr(lst)
    return fai

T = int(input())
for test_case in range(1, T+1):
    NX = list(map(int,input().split()))
    mat = []
    for AA in range(NX[0]):
        mat.append(list(map(int,input().split())))
    total = 0
    for Xsis in mat:
        AA = [0]*NX[0]
        if forwbackw(Xsis) == 0:
            total += 1
    for xi in range(NX[0]):
        AA = [0]*NX[0]
        Ysis = []
        for yi in range(NX[0]):
            Ysis.append(mat[yi][xi])
        if forwbackw(Ysis) == 0:
            total += 1
    print('#{0} {1}'.format(test_case,total))