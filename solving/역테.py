T = int(input())
for test_case in range(1,T+1):
    dmty = list(map(int,input().split()))
    day = dmty[0]
    month = dmty[1]
    three_month = dmty[2]
    year = dmty[3]
    fee = list(map(int,input().split()))
    pay = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pay_month = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    top_dis = 0
    for i in range(len(fee)):
        if fee[i] > 0:
            if day * fee[i] > month:
                pay[i] = month
            else:
                pay[i] = day * fee[i]

    for j in range(len(fee)-2):
        if pay[j]+pay[j+1]+pay[j+2] > three_month:
            pay_month[j] = three_month - (pay[j]+pay[j+1]+pay[j+2])
    if pay[10]+pay[11] > three_month:
        pay_month[10] = three_month - (pay[10]-pay[11])
    if pay[11] > three_month:
        pay_month[11] = three_month - pay[11]
    while sum(pay_month) < 0:
        min_month = []
        min_fee = 0
        for a in range(len(pay_month)):
            if pay_month[a] == min(pay_month):
                min_month.append(a)
            dis = [0,0]
        for a in min_month :
            if a > 0:
                min_fee += pay_month[a-1]
            if a > 1:
                min_fee += pay_month[a-2]
            if a < 10:
                min_fee += pay_month[a+2]
            if a < 11:
                min_fee += pay_month[a+1]
            if dis[0] == 0:
                dis = [min_fee, a]
            if dis[0] < min_fee:
                dis = [min_fee, a]
        top_dis += pay_month[dis[1]]
        for del_mon in range(dis[1]-2, dis[1]+3):
            if 0 <= del_mon < 12:
                pay_month[del_mon] = 0
    total = sum(pay)+top_dis
    if total > year:
        total = year
    print('#{0} {1}'.format(test_case,total))