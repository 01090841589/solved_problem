
def inpu(M) :
    r = []
    load = []
    r = input().split()
    r = list(map(int,r))
    for i in range(M) :
        n = input().split()
        n = list(map(int,n))
        load.append(n)
    return r,load

def cal(r, load, M) :
    for j in range(len(load)):
        if load[j][0] > load[j][1]:
            load[j][0], load[j][1] = load[j][1], load[j][0]
    load.sort()
    went = []
    check_point = 0
    least_go = 100
    gone = []
    for now in r:
        for chal in range(M):
            for i in range(len(load)):
                if now == load[i][0]:
                    if now in r:
                        went.append(now)
                    check_point += load[i][2]
                    now = load[i][1]
                    gone.append(load[i])
                    if now in r:
                        went.append(now)
                elif now == load[i][1]:
                    if now in r:
                        went.append(now)
                    check_point += load[i][2]
                    now = load[i][0]
                    gone.append(load[i])
                    if now in r:
                        went.append(now)
                compa = [A for A in r if A in went]
                if compa == r:
                    break
            if least_go > check_point:
                if compa == r:
                    least_go = check_point
            went = []
            check_point = 0
            now = r[0]
            if gone != []:
                load.remove(gone[0])
                load.append(gone[0])
            gone = []
    return least_go

T = int(input())
for i in range(T) :
    N, M, R = input().split()
    N = int(N)
    M = int(M)
    R = int(R)
    r, load = inpu(M)
    print('#{0} {1}'.format(i+1, cal(r,load,M)))