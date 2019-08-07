T = int(input())
for test_case in range(1, T+1):
    V, E = map(int,input().split())
    route = []
    visit = []
    stack = []
    for i in range(E):
        route.append(list(map(int,input().split())))
    S, G = map(int,input().split())
    visit.append(S)
    stack.append(S)
    while True:
        cnt = 0
        for i in route:
            if S == i[0]:
                if i[1] in visit:
                    continue
                visit.append(i[1])
                stack.append(i[1])
                cnt += 1
                S = i[1]
                break
        if S == G:
            print('#{} 1'.format(test_case))
            break
        if cnt == 0:
            if len(stack) > 0:
                S = stack.pop()
            else :
                print('#{} 0'.format(test_case))
                break
