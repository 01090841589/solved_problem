NX = [10, 2]
mat = [
[2, 2, 3, 5, 3, 1, 1, 1, 1, 1],
[2, 2, 3, 5, 3, 1, 1, 1, 1, 1],
[3, 3, 4, 5, 4, 3, 2, 1, 1, 2],
[3, 3, 4, 5, 4, 3, 2, 1, 1, 2],
[5, 5, 5, 5, 5, 5, 3, 1, 1, 3],
[4, 4, 4, 5, 5, 5, 4, 3, 3, 3],
[4, 4, 4, 5, 5, 5, 5, 5, 5, 3],
[4, 4, 4, 4, 4, 5, 5, 5, 5, 3],
[4, 4, 4, 4, 4, 5, 5, 5, 5, 3],
[5, 5, 4, 4, 4, 5, 5, 5, 5, 4]
]

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
    print(fai)
    return fai
total = 0
for Xsis in mat:
    AA = [0]*NX[0]
    print(Xsis,end=' ')
    if forwbackw(Xsis) == 0:
        total += 1
print()
for xi in range(NX[0]):
    AA = [0]*NX[0]
    Ysis = []
    for yi in range(NX[0]):
        Ysis.append(mat[yi][xi])
    print(Ysis,end=' ')
    if forwbackw(Ysis) == 0:
        total += 1
print('#{0} {1}'.format(total,total))
# 20190605 연속해서 7번 해결해야함