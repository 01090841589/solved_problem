
def MOVE(loca, c):
    Y = loca[0] + DIR[c][0]
    X = loca[1] + DIR[c][1]
    if 0 <= X < 10 and 0 <= Y < 10:
        return [Y, X]
def charge(loca, L, chg):
    for ap_num, ap in enumerate(AP):
        print(ap[2], [loca[0],(ap[1]-1)], [loca[1],(ap[0]-1)])
        if ap[2] >= abs(loca[0]-(ap[1]-1))+abs(loca[1]-(ap[0]-1)):
            print('{},{}'.format(L+1, ap_num))
            print([ap[2],ap[3]])
            chg[L].extend([ap_num,ap[3]])
    return True
def compare(chg):
    tot = 0
    for k, AB in enumerate(chg):
        if AB == []:
            chg[k].extend([-1, 0])
    for AA in range(len(chg[0]) // 2):
        for BB in range(len(chg[1]) // 2):
            if chg[0][AA * 2] == chg[1][BB * 2]:
                print(chg[0][AA * 2 + 1] // 2, chg[1][BB * 2 + 1] // 2)
                val = chg[0][AA * 2 + 1] // 2 + chg[1][BB * 2 + 1] // 2
            else:
                print(chg[0][AA * 2 + 1], chg[1][BB * 2 + 1])
                val = chg[0][AA * 2 + 1] + chg[1][BB * 2 + 1]
            if tot < val:
                tot = val
    print(tot)
    return tot
DIR = [[0,0], [-1,0], [0,1], [1,0], [0,-1]]
loc = [[0,0], [9,9]]
T = int(input())
for test_case in range(1, T+1):
    MA = list(map(int,input().split()))
    mov = []
    AP = []
    for moves in range(2):
        mov.append(list(map(int,input().split())))
    for APs in range(MA[1]):
        AP.append(list(map(int,input().split())))
    total = 0



    for i in range(MA[0]+1):
        charging = [[], []]
        for L in range(2):
            charge(loc[L], L, charging)
            if i < MA[0]:
                loc[L] = MOVE(loc[L], mov[L][i])
        total += compare(charging)
    print('#{0} {1}'.format(test_case,total))