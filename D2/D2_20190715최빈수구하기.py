def cal():
    a = input().split()
    a = list(map(int, a))
    A = []
    for i in range(100, -1, -1):
        A.append([0, i])
    for i in a:
        A[100 - i][0] += 1

    A = max(A)
    return A[1]


T = int(input())
for j in range(T) :
    C = int(input())
    A = cal()
    print('#{0} {1}'.format(C,A))