def change(N) :
    ex = [0,0,0,0,0,0,0,0]
    for i in range(len(money)) :
        if N >= money[i] :
            ex[i] = N // money[i]
            N = N % money[i]
    # if N > 0 :
    #     ex[i] += 1
    return ex

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for i in range(T) :
    N = int(input())
    cha = change(N)
    print('#{0}'.format(i+1))
    for i in range(len(cha)) :
        print('{0}'.format(cha[i]),end=' ')
    print('')