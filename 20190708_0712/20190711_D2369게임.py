a = int(input())

for i in range(1,a+1):
    cal_10 = 0
    cal_1 = 0
    if 100 <= i < 1000:
        cal_1 = i % 10
        cal_10 = i // 10
        cal_100 = cal_10 // 10
        cal_10 = cal_10 % 10

        if cal_100 == 3 or cal_100 == 6 or cal_100 == 9 :
            print('-',end=' ')
        elif cal_10 == 3 or cal_10 == 6 or cal_10 == 9 :
            print('-', end=' ')
        elif cal_1 == 3 or cal_1 == 6 or cal_1 == 9 :
            print('-', end=' ')
        else :
            print('{0}{1}{2}'.format(cal_100,cal_10,cal_1),end='')
    if 10<= i < 100:
        cal_1 = i % 10
        cal_10 = i // 10
        if cal_10 == 3 or cal_10 == 6 or cal_10 == 9 :
            if cal_1 == 3 or cal_1 == 6 or cal_1 == 9:
                print('--', end=' ')
            else :
                print('-',end=' ')
        elif cal_1 == 3 or cal_1 == 6 or cal_1 == 9 :
            print('-',end=' ')
        else :
            print('{0}{1}'.format(cal_10,cal_1),end=' ')
    if i < 10 :
        if i % 3 == 0 :
            print('-',end = ' ')
        else :
            print(i,end = ' ')