T = int(input())
for c in range(T) :
    N = int(input())
    A = []
    for i in range(N) :
        a = int(input())
        if A == [] :
            A.append(a)
        elif a in A :
            A.remove(a)
        else :
            A.append(a)
    print('#{0} {1}'.format(c+1,len(A)))