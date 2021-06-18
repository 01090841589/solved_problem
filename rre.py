def solution(n, start, end, roads, traps):
    for i in range(len(traps)):
        traps[i] -= 1
    def mage(now, k, evers):
        if now == end-1:
            return
        if not evers[now]:
            for i in range(len(MAP[now])):
                if MAP[now][i] > 0:
                    if k+MAP[now][i] < visited[i][evers[i]]:
                        visited[i][evers[i]] = k + MAP[now][i]
                        if i in traps:
                            evers[i] = (evers[i] + 1 + evers[now]) % 2
                            mage(i, k + MAP[now][i], evers)
                        else:
                            mage(i, k + MAP[now][i], evers)
        else:
            for i in range(len(MAP[now])):
                if MAP[now][i] < 0:
                    if k+(MAP[now][i]*-1) < visited[i][evers[i]]:
                        visited[i][evers[i]] = k + (MAP[now][i]*-1)
                        if i in traps:
                            evers[i] = (evers[i] + 1 + evers[now]) % 2
                            mage(i, k+(MAP[now][i]*-1), evers)
                        else:
                            mage(i, k+(MAP[now][i]*-1), evers)


    MAP = [[0] * n for _ in range(n)]
    rat = [0] * n
    visited = [[999999] * 2 for _ in range(n)]
    for road in roads:
        if not MAP[road[0]-1][road[1]-1]:
            MAP[road[0]-1][road[1]-1] = road[2]
            MAP[road[1]-1][road[0]-1] = -road[2]
        else:
            if MAP[road[0]-1][road[1]-1] > road[2]:
                MAP[road[0]-1][road[1]-1] = road[2]
                MAP[road[1]-1][road[0]-1] = -road[2]
    visited[start-1][0] = 0
    mage(start-1, 0, [0]*n)


    # print(visited)
    answer = min(visited[end-1])
    return answer



# print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2, 3]))