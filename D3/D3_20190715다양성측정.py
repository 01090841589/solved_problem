

def cal_num(num) :
    check = []
    while num > 0 :
        a = num % 10
        num = num//10
        check.append(a)
    check = list(set(check))
    return check

N = int(input())
for i in range(N) :
    num = int(input())
    check = cal_num(num)
    print('#{0} {1}'.format(i+1,len(check)))