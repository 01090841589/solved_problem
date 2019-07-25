def locate_search(pyramid, a):
    for i in range(len(pyramid)):
        if pyramid[i][0] <= a <= pyramid[i][-1]:
            for j in range(len(pyramid[i])):
                if pyramid[i][j] == a:
                    return i, j
T = int(input())
for test_case in range(1, T+1):
    pyramid = []
    floor = 1
    floor_ele = []
    i = 1
    a, b = map(int,input().split())
    n = max(a, b)
    while i <= n:
        for element in range(i, floor+i):
            floor_ele.append(i)
            i += 1
        floor += 1
        pyramid.append(floor_ele)
        floor_ele = []
    # for i in range(len(pyramid)):
    #     print(pyramid[i])
    my_locate = locate_search(pyramid, a)
    trasure = locate_search(pyramid, b)
    if my_locate[0] > trasure[0]:
        my_locate, trasure = trasure, my_locate
    cnt = 0
    if trasure[0] >= my_locate[0]:
        cnt += trasure[0] - my_locate[0]
        if trasure[1]-my_locate[1] < 0:
            cnt += abs(trasure[1]-my_locate[1])
        elif trasure[1]-my_locate[1] > trasure[0] - my_locate[0]:
            cnt += ((trasure[1]-my_locate[1]) - (trasure[0] - my_locate[0]))
    print('#{0} {1}'.format(test_case,cnt))