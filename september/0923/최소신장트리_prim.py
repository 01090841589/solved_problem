import sys
sys.stdin = open('최소신장트리.txt')


def prim(k, cnt):
    if k == V:
        print('#{} {}'.format(tc, cnt))
        return
    val = []
    for a in prim_lst:
        for i in range(V+1):
            if MAP[a][i] and visited[i] == 0:
                if val == []:
                    val = [i, MAP[a][i]]
                else:
                    if val[1] > MAP[a][i]:
                        val[0] = i
                        val[1] = MAP[a][i]
    prim_lst.append(val[0])
    visited[val[0]] = 1
    return prim(k+1, cnt+val[1])


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    MAP = [[0] * (V+1) for _ in range(V+1)]
    for c in node:
        MAP[c[0]][c[1]] = c[2]
        MAP[c[1]][c[0]] = c[2]
    visited = [0]*(V+1)
    prim_lst = [0]
    visited[0] = 1
    prim(0, 0)
