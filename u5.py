M = 16
r = [1, 2, 3, 4, 5, 6]
load = [[1, 2, 4], [2, 3, 3],[4, 3, 7], [1, 4, 6], [4, 2, 2], [3, 1, 6],[1, 5, 5],[2, 5, 3],[3, 5, 8], [4, 5, 4],[1, 6, 3], [2, 6, 2], [3, 6, 5], [4, 6, 5],[5, 6, 7]]


for j in range(len(load)):
    if load[j][0] > load[j][1]:
        load[j][0], load[j][1] = load[j][1], load[j][0]
load.sort()
went = []
check_point = 0
least_go = 100
gone = []
for now in r :
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
            print(compa,check_point)
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
    print(least_go)