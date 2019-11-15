def devide(k, first, second):
    global result
    if k == M:
        scr = gostair(first, second)
        if result > scr:
            result = scr
        return
    devide(k+1, first+[people[k]], second)
    devide(k+1, first, second+[people[k]])


def gostair(first, second):
    global result
    wait1 = []
    wait2 = []
    for i in range(len(first)):
        wait1.append(abs(first[i][0]-stair[0][0])+abs(first[i][1]-stair[0][1])+1)
    for i in range(len(second)):
        wait2.append(abs(second[i][0]-stair[1][0])+abs(second[i][1]-stair[1][1])+1)
    wait1.sort()
    wait2.sort()
    scr1, scr2 = 0, 0
    while wait1:
        if result <= scr1:
            break
        scr1 = wait1.pop(0)+stair[0][2]
        if len(wait1) > 2:
            wait1[2] = max(scr1, wait1[2])
    while wait2:
        if result <= scr2:
            break
        scr2 = wait2.pop(0)+stair[1][2]
        if len(wait2) > 2:
            wait2[2] = max(scr2, wait2[2])
    return max(scr1, scr2)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    people = []
    stair = []
    for y in range(N):
        for x in range(N):
            if MAP[y][x] == 1:
                people.append([y, x])
            elif MAP[y][x] > 1:
                stair.append(([y, x, MAP[y][x]]))
    M = len(people)
    result = N*N*M
    devide(0, [], [])
    print('#{} {}'.format(tc, result))