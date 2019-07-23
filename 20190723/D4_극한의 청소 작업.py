T = int(input())
for test_case in range(1,T+1):
    floor = input().split()
    floor = list(map(int,floor))
    total = 0
    minus = [0,0]
    if floor[0]<0:
        floor[0] = abs(floor[0])
        minus[0] = 1
    if floor[1]<0:
        floor[1] = abs(floor[1])
        minus[1] = 1
    for i in range(2):
        a = 1
        while floor[i] > 0 :
            if floor[i] % 10 > 4:
                total += (floor[i]%10-1) * a
                a *= 9
                floor[i] //= 10
            else:
                total += (floor[i]%10) * a
                a *= 9
                floor[i] //= 10
        floor[i] = total
        total = 0
    if minus[0] == 1:
        floor[0] *= -1
        if minus[1] == 0:
            total -= 1
        else:
            floor[1] *= -1
    total += floor[1]-floor[0]
    print('#{0} {1}'.format(test_case,total))


