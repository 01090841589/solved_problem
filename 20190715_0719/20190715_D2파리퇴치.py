def arrr(N) :
    for i in range(N) :
        inp = input().split(' ')
        inp = [int(j) for j in inp]
        fly.append(inp)
    return fly

def max_cal(fly,N,M):
    sum_num = 0
    max_num = 0
    for i in range(N-M+1) :
        for j in range(N-M+1) :
            for l in range(M) :
                for m in range(M) :
                    sum_num += fly[l+i][m+j]
            if max_num < sum_num :
                max_num = sum_num
            sum_num = 0
    return(max_num)

T = int(input())
for a in range(T):
    N = input().split(' ')
    fly = []
    fly = arrr(int(N[0]))
    print('#{0} {1}'.format(a+1, max_cal(fly,int(N[0]),int(N[1]))))