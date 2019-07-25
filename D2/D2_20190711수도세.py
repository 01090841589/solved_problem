T = int(input())
A = []
for i in range(T) :
    A.append(input().split(' '))

def water_fee(price) :
    #A사 = 리터당 P원
    #B사 = R리터이하 기본요금Q원, 초과요금 Q+S원
    #사용하는 수도양 W
    P = int(price[0])
    Q = int(price[1])
    R = int(price[2])
    S = int(price[3])
    W = int(price[4])
    A_COM = P*W
    B_COM = Q
    if W > R :
        B_COM += (W-R)*S
    if A_COM <= B_COM :
        return A_COM
    else :
        return B_COM

for i in range(0,T) :
    print('#{0} {1}'.format(i+1, water_fee(A[i])))

