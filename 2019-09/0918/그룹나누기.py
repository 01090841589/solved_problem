import sys
sys.stdin = open("그룹나누기.txt")


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    node = list(map(int, input().split()))
    visited = [i for i in range(N+1)]

    for i in range(M):
        low = min(node[i*2], node[(i*2)+1])
        high = max(node[i*2], node[(i*2)+1])
        if visited[low] == visited[high]:
            continue
        if visited[high] != visited[low]:
            a = visited[high]
            for j in range(N+1):
                if visited[j] == a:
                    visited[j] = visited[low]
    cnt = 0
    for k in range(1, N+1):
        if visited[k] == k:
            cnt += 1
    print('#{} {}'.format(tc, cnt))