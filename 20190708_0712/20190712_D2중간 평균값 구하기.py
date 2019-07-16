
def mid_num(A):
    B = []
    for i in range(len(A)):
            B.append(int(A[i]))
    B.sort()
    del B[len(B)-1]
    del B[0]
    b = round(sum(B)/len(B))
    return b

T = int(input())
for i in range(T):
    A = input().split(' ')
    print(A)
    print('#{0} {1}'.format(i+1,mid_num(A)))

