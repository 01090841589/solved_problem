def cal_sudo(sudo) :
    test = []
    result = 1
    for a in range(9):
        for b in range(9):
            test.append(sudo[a][b])
        test.sort()
        test = list(set(test))
        if len(test) != 9 :
            result = 0
        test = []
    for b in range(9):
        for a in range(9):
            test.append(sudo[a][b])
        test.sort()
        test = list(set(test))
        if len(test) != 9 :
            result = 0
        test = []
    for i in range(0,9,3) :
        for j in range(0,9,3) :
            for a in range(i, 3+i, 1) :
                for b in range(j, 3+j, 1):
                    test.append(sudo[a][b])
            test.sort()
            test = list(set(test))
            if len(test) != 9:
                result = 0
            test = []
    return result
T = int(input())
for con in range(T) :
    sudo = []
    for i in range(9) :
        num = input().split(' ')
        num = [x for x in num if x]
        num = list(map(int,num))
        sudo.append(num)
    print('#{0} {1}'.format(con+1,cal_sudo(sudo)))