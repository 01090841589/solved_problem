T = int(input())



def madi(Mes) :
    L = []
    M = []
    for i in range(len(Mes)) :
        L.append(Mes[i])
    i = 0
    while i < 11 :
        M_pare = L
        M_pare2 = []
        M.append(Mes[i])
        for j in range(len(M)) :
            if M[j] == M_pare[j] :
                M_pare.append(M_pare[j])
        for k in range(i) :
            if M[i] == M_pare[i] :
                if M[0] == M_pare[i+1] :
                    if M[1] == M_pare[i+2] :
                        return len(M)
            else :
                break
        i += 1
    return len(M)
for i in range(T):
    Mes = input()
    print('#{0} {1}'.format(i+1, madi(Mes))