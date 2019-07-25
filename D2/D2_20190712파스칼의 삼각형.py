T = int(input())


def tri_num(N) :
    a = [1]
    print(a[0])
    for j in range(N):
        b = []
        b.append(1)
        for i in range(j) :
            if i == j-1 :
                b.append(1)
                a = b
                b = []
                for k in range(len(a)) :
                    if k == len(a)-1 :
                        print(a[k])
                    else :
                        print(a[k],end=' ')
            else :
                b.append(a[i+1]+a[i])

    return

for i in range(T) :
    N = int(input())
    print('#{0}'.format(i+1))
    tri_num(N)