import sys
sys.stdin = open("서로소.txt")


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cal = [list(map(int, input().split())) for _ in range(M)]
    # node = [i for i in range(1000001)]
    visited = [-1] * 100
    stack = []
    for d in cal:
        if d[1] == d[2]:
            continue
        if d[0] == 0:
            # if visited[max(d[1], d[2])] != max(d[1], d[2]):
            #     visited[visited[max(d[1], d[2])]] = visited[min(d[1], d[2])]
            if visited[min(d[1], d[2])] == -1:
                visited[max(d[1], d[2])] = min(d[1], d[2])
            else:
                k = visited[min(d[1], d[2])]
                while visited[k] != -1:
                    k = visited[k]
                    print(k)
                visited[d[1]] = k
                visited[d[2]] = k
        # if d[0] == 1:
        #     if visited(d[1])
    # for i in range(1, 100):
    #     if visited[i] != i:
    #         visited[i] = visited[visited[i]]
    print(visited)
    print(stack)