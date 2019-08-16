def route(visit, cnt, queue):
    for fin in range(len(queue)):
        A = queue.pop(0)
        visit[A-1] = 1
        for i, j in enumerate(node):
            if A in j:
                if visit[j[(j.index(A) + 1) % 2]-1] == 0:
                    queue.append(j[(j.index(A) + 1) % 2])
    cnt += 1
    if G in queue:
        print('#{} {}'.format(test_case,cnt))
        return
    if len(queue) > 0 :
        route(visit, cnt, queue)
    elif len(queue) == 0:
        print('#{} 0'.format(test_case))
    return
T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    node = []
    [node.append(list(map(int, input().split()))) for i in range(E)]
    S, G = map(int, input().split())
    cnt = 0
    visit = [0]*V
    queue = [S]
    route(visit, cnt, queue)