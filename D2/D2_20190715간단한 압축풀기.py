def inp_str(N) :
    str_num = []
    for i in range(N) :
        num = input().split(' ')
        num[1] = int(num[1])
        str_num.append(num)
    return str_num

def cal_str(str_num,N) :
    enter = 10
    for i in range(N) :
        rest = str_num[i][1]
        while rest > 0 :
            print(str_num[i][0],end = '')
            rest -= 1
            enter -= 1
            if enter == 0 :
                print('')
                enter = 10

T = int(input())
for a in range(T) :
    N = int(input())
    str_num = inp_str(N)
    print('#{0}'.format(a+1))
    cal_str(str_num,N)
    print('')
