
def plus_time() :
    time = []
    time = input().split(' ')
    time = list(map(int,time))
    cal_time = [0,0]
    cal_time[0] = time[0]+time[2]
    cal_time[1] = time[1]+time[3]
    if cal_time[1]>= 60 :
        cal_time[1] -= 60
        cal_time[0] += 1
    if cal_time[0] > 12 :
        cal_time[0] -=12
    return cal_time

T = int(input())
for i in range(T) :
    cal_time = plus_time()
    print('#{0} {1} {2}'.format(i+1, cal_time[0], cal_time[1]))