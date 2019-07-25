def poww(n,m):
    if m == 1:
        return n
    return n * poww(n,m-1)
for i in range(1,11):
    T = int(input())
    N = list(map(int,input().split()))
    print('#{0} {1}'.format(i,poww(N[0],N[1])))
