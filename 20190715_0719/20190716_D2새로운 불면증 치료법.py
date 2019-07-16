T = int(input())
for j in range(1, T+1) :
    N = int(input())
    n = []
    i = 0
    while len(n) < 10 :
        i += 1
        num = N*i
        while num > 0 :
            n.append(num % 10)
            num //= 10
            n = list(set(n))
    print('#{0} {1}'.format(j, N*i))