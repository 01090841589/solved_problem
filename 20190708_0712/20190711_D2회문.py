T = int(input())
A = []
for i in range(T) :
    A.append(input())

def ped(word) :
    pare_a = []
    pare_b = []
    for i in range(len(word)-1) :
        pare_a.append(word[i])
        pare_b.append(word[(len(word)-i-1)])
    if pare_a == pare_b :
        return 1
    else :
        return 0
for i in range(0,T) :
    print('#{0} {1}'.format(i+1, ped(A[i])))