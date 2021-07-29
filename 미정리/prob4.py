
def solution(n, start, end, roads, traps):
    for i in range(len(traps)):
        traps[i] -= 1
    def mage(now, k):
        if now == end-1:
            return
        for nowed in MAP[now]:
            if nowed[1] > 0 and (evers[now]+evers[nowed[0]]) % 2 == 0:
                if k+nowed[1] < visited[nowed[0]][evers[nowed[0]] % 2]:
                    visited[nowed[0]][(evers[now]+evers[nowed[0]]) % 2] = k + nowed[1]
                    if nowed[0] in traps:
                        evers[nowed[0]] += 1
                        mage(nowed[0], k + nowed[1])
                        evers[nowed[0]] -= 1
                    else:
                        mage(nowed[0], k + nowed[1])
            elif nowed[1] < 0 and (evers[now]+evers[nowed[0]]) % 2:
                if k+(nowed[1]*-1) < visited[nowed[0]][evers[nowed[0]] % 2]:
                    visited[nowed[0]][(evers[now]+evers[nowed[0]]) % 2] = k + (nowed[1]*-1)
                    if nowed[0] in traps:
                        evers[nowed[0]] += 1
                        mage(nowed[0], k+(nowed[1]*-1))
                        evers[nowed[0]] -= 1
                    else:
                        mage(nowed[0], k+(nowed[1]*-1))


    MAP = [[] * n for _ in range(n)]
    visited = [[999999] * 2 for _ in range(n)]
    evers = [0] * n
    for road in roads:
        MAP[road[0]-1].append([road[1]-1, road[2]])
        MAP[road[1]-1].append([road[0]-1, -road[2]])
    visited[start-1][0] = 0
    mage(start-1, 0)
    answer = min(visited[end-1])
    return answer



print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
print(solution(4,1,3,[[1, 2, 2], [2, 3, 3], [1, 4, 1], [4, 3, 1]],[]))
# print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2, 3]))
# print(solution(7,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1], [3, 5, 1], [6, 5, 1], [2, 6, 2], [7, 2, 2]],[2, 5, 7]))