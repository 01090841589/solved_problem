

date = [[1, 31], [2, 28], [3, 31], [4, 30], [5, 31], [6, 30], [7, 31], [8, 31], [9, 30], [10, 31], [11, 30], [12, 31]]
cal = [[2, 21], [4, 1]]
def sub_date(cal) :
    total = 0
    while cal[0] < cal[2] :
        total += (date[cal[0]-1][1]-cal[1])
        total += 1
        cal[0] += 1
        cal[1] = 1
    if cal[2] == cal[0] :
        total += cal[3] - cal[1]
        total += 1
    return total
T = int(input())
for i in range(T) :
    inp = input().split(' ')
    cal = list(map(int,inp))
    print('#{0} {1}'.format(i+1,sub_date(cal)))