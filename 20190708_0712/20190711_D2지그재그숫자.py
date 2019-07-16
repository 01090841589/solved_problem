A = int(input())
B = []
for i in range(A) :
    B.append(int(input()))

for i in range(A) :
    num = 0
    for j in range(1,B[i]+1):
        if j % 2 == 1 :
            num += j
        else :
            num -= j
    print('#{0} {1}'.format(i+1,num))