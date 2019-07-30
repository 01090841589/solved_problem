N = list(map(int,input().split()))
contect = [1, 17, 3, 22, 1, 8, 1, 7, 7, 1, 2, 7, 2, 15, 15, 4, 6, 2, 11, 6, 4, 10, 4, 2]
contect = list(map(int, input().split()))
connecter = [N[1]]
route = []
result = [N[1]]
반복 = 0
while 반복 != len(result):
    반복 = len(result)
    for AA in range(0, len(contect), 2):
        for 연락할애들 in connecter:
            if 연락할애들 == contect[AA]:
                route.append(contect[AA+1])
                route.sort()
    result += route
    result = list(set(result))
    result.sort()
    connecter = route[:]
    route = []
    print(connecter)
    print(route)
    print(result)
print(max(result))