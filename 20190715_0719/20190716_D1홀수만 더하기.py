T = int(input())
for test_case in range(1, T+1):
    total = 0
    num = input().split(' ')
    num = list(map(int,num))
    for i in num :
        if i % 2 == 1:
            total += i
    print('#{0} {1}'.format(test_case,total))