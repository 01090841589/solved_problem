def cal_sum(month,total):
    global min_sum
    if month >= 12:
        min_sum = min(min_sum,total)
    else:
        if M[month]*N[0] >= N[1]:
            value = N[1]
        else:
            value = M[month] * N[0]
        cal_sum(month+1,total+value)
        cal_sum(month+3,total+N[2])

T = int(input())
for test_case in range(1, T+1):
    N = list(map(int,input().split()))
    M = list(map(int,input().split()))
    min_sum = N[3]
    cal_sum(0,0)
    print('#{0} {1}'.format(test_case,min_sum))