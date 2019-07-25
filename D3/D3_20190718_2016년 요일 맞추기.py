date = [[1, 31], [2, 29], [3, 31], [4, 30], [5, 31], [6, 30], [7, 31], [8, 31], [9, 30], [10, 31], [11, 30], [12, 31]]
def sub_date(cal) :
    total = 0
    while cal[0][0] < cal[1][0] :
        total += (date[cal[0][0]-1][1])
        cal[0][0] += 1
        cal[0][1] = 1
    if cal[1][0] == cal[0][0] :
        total += cal[1][1] - cal[0][1]
    return total
T = int(input())
for test_case in range(1,T+1) :
    cal = [[1, 1]]
    inp = input().split(' ')
    cal.append(list(map(int,inp)))
    day = (4+sub_date(cal))%7
    print('#{0} {1}'.format(test_case,day))