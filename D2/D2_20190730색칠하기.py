T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cnt = 0
    red = []
    blue = []
    for i in range(N):
        rect = list(map(int,input().split()))
        if rect[4] == 1:
            for y in range(rect[0],rect[2]+1):
                for x in range(rect[1], rect[3]+1):
                    if [x, y] not in red:
                        red.append([x, y])
        else:
            for y in range(rect[0],rect[2]+1):
                for x in range(rect[1], rect[3]+1):
                    if [x, y] not in blue:
                        blue.append([x, y])
    for i in red:
        if i in blue:
            cnt+=1
    print('#{0} {1}'.format(test_case,cnt))