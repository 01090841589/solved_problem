NX = [9, 2]
A = [1, 1, 2, 2, 3, 3, 4, 3, 3]

def corr(lst):
    temp = 0
    fail = 0
    for i,j in enumerate(lst):
        if i == 0:
            temp = j
        elif temp > j :
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
        elif temp < j:
            temp = j
    return fail

AA = [0]*NX[0]
print(corr(A))