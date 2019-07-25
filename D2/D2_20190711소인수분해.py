T = int(input())
A = []
for i in range(T) :
    A.append(input())

def soinsu(num):
    key = int(num)
    b,c,d,e,f = 0,0,0,0,0
    while key % 2 == 0 :
        key = key // 2
        b += 1
    while key % 3 == 0 :
        key = key // 3
        c += 1
    while key % 5 == 0 :
        key = key // 5
        d += 1
    while key % 7 == 0 :
        key = key // 7
        e += 1
    while key % 11 == 0 :
        key = key // 11
        f += 1
    return b,c,d,e,f

for i in range(0,T):
    result = soinsu(A[i])
    print('#{0} '.format(i+1),end='')
    for j in range(0,5):
        print(result[j],end=' ')
    print('\n')