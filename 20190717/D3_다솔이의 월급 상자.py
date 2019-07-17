T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    total = 0
    for i in range(N):
        money = input().split()
        money = list(map(float,money))
        cal_money = money[0] * money[1]
        total += cal_money
    print('#{0} {1}'.format(test_case,total))