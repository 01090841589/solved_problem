T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    bus = []
    for i in range(N):
        route = input().split(' ')
        route = list(map(int,route))
        bus.append(route)
    P = int(input())
    C = []
    for c in range(P):
        C.append(int(input()))
    node = []
    for a in range(len(C)):
        node.append(0)

    for i in range(N):
        for stop in range(len(C)):
            if C[stop] in range(bus[i][0], bus[i][1]+1):
                node[stop] += 1
    print('#{0}'.format(test_case),end=' ')
    for cal in range(P):
        if cal == P-1 :
            print(node[cal])
        else :
            print(node[cal],end=' ')